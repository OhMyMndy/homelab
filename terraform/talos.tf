# remove all talos resources: cat terraform.tfstate | jq -r '.resources | .[] | select(.type,.name | match("talos")) | .type + "." + .name' | xargs -I{} bash -c "echo {}; tofu state rm '{}'"
locals {
  node_name         = "pve-1"
  datastore_id      = "local-zfs"
  controlplane_1_ip = "10.0.40.66"
  worker_1_ip       = "10.0.40.69"
  cluster_name      = "homelab"
}
resource "talos_machine_secrets" "machine_secrets" {}

data "talos_client_configuration" "talosconfig" {
  cluster_name         = local.cluster_name
  client_configuration = talos_machine_secrets.machine_secrets.client_configuration
  endpoints            = [local.controlplane_1_ip]
}

data "talos_machine_configuration" "machineconfig_cp" {
  cluster_name     = local.cluster_name
  cluster_endpoint = "https://${local.controlplane_1_ip}:6443"
  machine_type     = "controlplane"
  machine_secrets  = talos_machine_secrets.machine_secrets.machine_secrets
}

resource "talos_machine_configuration_apply" "cp_config_apply" {
  depends_on                  = [proxmox_virtual_environment_vm.talos_controlplane_1]
  client_configuration        = talos_machine_secrets.machine_secrets.client_configuration
  machine_configuration_input = data.talos_machine_configuration.machineconfig_cp.machine_configuration
  count                       = 1
  node                        = local.controlplane_1_ip
}

data "talos_machine_configuration" "machineconfig_worker" {
  cluster_name     = local.cluster_name
  cluster_endpoint = "https://${local.controlplane_1_ip}:6443"
  machine_type     = "worker"
  machine_secrets  = talos_machine_secrets.machine_secrets.machine_secrets
}

resource "talos_machine_configuration_apply" "worker_config_apply" {
  depends_on                  = [proxmox_virtual_environment_vm.talos_worker_1]
  client_configuration        = talos_machine_secrets.machine_secrets.client_configuration
  machine_configuration_input = data.talos_machine_configuration.machineconfig_worker.machine_configuration
  count                       = 1
  node                        = local.worker_1_ip
}

resource "talos_machine_bootstrap" "bootstrap" {
  depends_on           = [talos_machine_configuration_apply.cp_config_apply]
  client_configuration = talos_machine_secrets.machine_secrets.client_configuration
  node                 = local.controlplane_1_ip
}

data "talos_cluster_health" "health" {
  depends_on           = [talos_machine_configuration_apply.cp_config_apply, talos_machine_configuration_apply.worker_config_apply]
  client_configuration = data.talos_client_configuration.talosconfig.client_configuration
  control_plane_nodes  = [local.controlplane_1_ip]
  worker_nodes         = [local.worker_1_ip]
  endpoints            = data.talos_client_configuration.talosconfig.endpoints
}

resource "talos_cluster_kubeconfig" "kubeconfig" {
  depends_on           = [talos_machine_bootstrap.bootstrap, data.talos_cluster_health.health]
  client_configuration = talos_machine_secrets.machine_secrets.client_configuration
  node                 = local.controlplane_1_ip
}

# resource "proxmox_virtual_environment_vm" "talos_1_9_3_template" {
#   name        = "talos-1-9-3-template"
#   description = "Managed by Terraform"
#   tags        = ["terraform", "talos", "template"]
#   vm_id       = 9001
#
#   node_name = local.node_name
#
#   agent {
#     # read 'Qemu guest agent' section, change to true only when ready
#     enabled = false
#     trim    = true
#   }
#
#   initialization {
#     datastore_id = local.datastore_id
#     ip_config {
#       ipv4 {
#         address = "dhcp"
#       }
#     }
#   }
#
#   machine = "q35"
#
#   operating_system {
#     type = "l26"
#   }
#
#   cpu {
#     # type    = "x86-64-v2-AES"
#     type    = "host"
#     sockets = 1
#     cores   = 1
#   }
#
#   memory {
#     dedicated = 2048
#   }
#
#   on_boot         = false
#   started         = false
#   template        = true
#   stop_on_destroy = true
#
#   disk {
#     datastore_id = local.datastore_id
#     file_id      = proxmox_virtual_environment_download_file.talos_1_9_3.id
#     interface    = "virtio0"
#     iothread     = false
#     discard      = "on"
#     size         = 20
#     file_format  = "raw"
#   }
#
#   network_device {
#     bridge = "vmbr0"
#   }
#
#   bios = "ovmf"
#
#   efi_disk {
#     file_format  = "raw"
#     type         = "4m"
#     datastore_id = local.datastore_id
#   }
#
#   tpm_state {
#     version = "v2.0"
#     datastore_id = local.datastore_id
#   }
#
#   lifecycle {
#     ignore_changes = [
#       started
#     ]
#   }
# }

resource "proxmox_virtual_environment_vm" "talos_controlplane_1" {
  name        = "talos-controlplane-1"
  description = "Managed by Terraform"
  tags        = ["terraform", "talos", "kubernetes"]

  vm_id     = 366
  node_name = local.node_name
  # bios      = "ovmf"
  # machine   = "q35"

  operating_system {
    type = "l26"
  }


  # pool_id = proxmox_virtual_environment_pool.eyedeck_pool.id

  agent {
    # read 'Qemu guest agent' section, change to true only when ready
    enabled = true
    # trim    = true
  }


  initialization {
    datastore_id = local.datastore_id
    # ip_config {
    #   ipv4 {
    #     address = "dhcp"
    #   }
    # }
    ip_config {
      ipv4 {
        address = "${local.controlplane_1_ip}/24"
        gateway = "10.0.40.1"
      }
    }

    dns {
      servers = ["10.0.40.4", "10.0.40.1"]
      domain  = "home.mndy.be"
    }
    # dns {
    #   servers = ["10.10.42.1"]
    #   domain  = "spyrja.internal"
    # }

  }

  # The Ubuntu 23.10 template only has a single core
  cpu {
    # type = "host"
    type = "x86-64-v2-AES"
    # flags   = ["+cx16", "+lahf_lm", "+popcnt", "+sse3", "+ssse3", "+sse4.1", "+sse4.2"]
    sockets = 1
    cores   = 2
  }

  memory {
    dedicated = 4100
  }
  started         = true
  on_boot         = true
  stop_on_destroy = true

  # disk {
  #   datastore_id = local.datastore_id
  #   interface    = "virtio0"
  #   iothread     = false
  #   discard      = "on"
  #   file_format  = "raw"
  #   size         = 60
  # }

  disk {
    datastore_id = local.datastore_id
    file_id      = proxmox_virtual_environment_download_file.talos_1_9_3.id
    interface    = "virtio0"
    file_format  = "raw"
    size         = 20
  }
  # For now, EyeDeck uses the same bridge, just has to set a vlan.
  # One day, I'll figure out how to create SDN zones and such with
  # the proxmox provider.
  network_device {
    bridge = "vmbr0"
    # vlan_id = "42"
  }

  lifecycle {
    ignore_changes = [
      started,
      initialization[0].user_data_file_id,
      clone[0].vm_id
    ]
  }
  # efi_disk {
  #   file_format  = "raw"
  #   type         = "4m"
  #   datastore_id = local.datastore_id
  # }
  #
  # tpm_state {
  #   version      = "v2.0"
  #   datastore_id = local.datastore_id
  # }
}


resource "proxmox_virtual_environment_vm" "talos_worker_1" {
  name        = "talos-worker-1"
  description = "Managed by Terraform"
  tags        = ["terraform", "talos", "kubernetes"]

  vm_id     = 369
  node_name = local.node_name
  # bios      = "ovmf"
  # machine   = "q35"

  operating_system {
    type = "l26"
  }


  # pool_id = proxmox_virtual_environment_pool.eyedeck_pool.id

  agent {
    # read 'Qemu guest agent' section, change to true only when ready
    enabled = true
    # trim    = true
  }


  initialization {
    datastore_id = local.datastore_id
    # ip_config {
    #   ipv4 {
    #     address = "dhcp"
    #   }
    # }
    ip_config {
      ipv4 {
        address = "${local.worker_1_ip}/24"
        gateway = "10.0.40.1"
      }
    }

    dns {
      servers = ["10.0.40.4", "10.0.40.1"]
      domain  = "home.mndy.be"
    }
    # dns {
    #   servers = ["10.10.42.1"]
    #   domain  = "spyrja.internal"
    # }

  }

  # The Ubuntu 23.10 template only has a single core
  cpu {
    # type = "host"
    type = "x86-64-v2-AES"
    # flags   = ["+cx16", "+lahf_lm", "+popcnt", "+sse3", "+ssse3", "+sse4.1", "+sse4.2"]
    sockets = 1
    cores   = 2
  }

  memory {
    dedicated = 4100
  }
  started         = true
  on_boot         = true
  stop_on_destroy = true

  # disk {
  #   datastore_id = local.datastore_id
  #   interface    = "virtio0"
  #   iothread     = false
  #   discard      = "on"
  #   file_format  = "raw"
  #   size         = 60
  # }

  disk {
    datastore_id = local.datastore_id
    file_id      = proxmox_virtual_environment_download_file.talos_1_9_3.id
    interface    = "virtio0"
    file_format  = "raw"
    size         = 20
  }
  # For now, EyeDeck uses the same bridge, just has to set a vlan.
  # One day, I'll figure out how to create SDN zones and such with
  # the proxmox provider.
  network_device {
    bridge = "vmbr0"
    # vlan_id = "42"
  }

  lifecycle {
    ignore_changes = [
      started,
      initialization[0].user_data_file_id,
      clone[0].vm_id
    ]
  }
}


output "talosconfig" {
  value = data.talos_client_configuration.talosconfig.talos_config
  sensitive = true
}

output "kubeconfig" {
  value = resource.talos_cluster_kubeconfig.kubeconfig.kubeconfig_raw
  sensitive = true
}
