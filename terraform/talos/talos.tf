# remove all talos resources: cat terraform.tfstate | jq -r '.resources | .[] | select(.type,.name | match("talos")) | .type + "." + .name' | xargs -I{} bash -c "echo {}; tofu state rm '{}'"
locals {
  node_name         = "pve-1"
  datastore_id      = "local-zfs"
  controlplane_1_ip = "10.0.40.66"
  worker_ips        = ["10.0.40.69", "10.0.40.70", "10.0.40.71"]
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
  config_patches = [
    templatefile("config-patch.yaml", {
    })
  ]
}

data "talos_machine_configuration" "machineconfig_worker" {
  cluster_name     = local.cluster_name
  cluster_endpoint = "https://${local.controlplane_1_ip}:6443"
  # cluster_endpoint = join(",", [for w in local.worker_ips: format("https://%q:443", w)])
  machine_type    = "worker"
  machine_secrets = talos_machine_secrets.machine_secrets.machine_secrets
}

resource "talos_machine_configuration_apply" "worker_config_apply" {
  for_each = {
    for index, i in local.worker_ips :
    index => i
  }
  depends_on                  = [proxmox_virtual_environment_vm.talos_worker]
  client_configuration        = talos_machine_secrets.machine_secrets.client_configuration
  machine_configuration_input = data.talos_machine_configuration.machineconfig_worker.machine_configuration
  node                        = each.value
  config_patches = [
    templatefile("config-patch.yaml", {
    })
  ]
}

resource "talos_machine_bootstrap" "bootstrap" {
  depends_on           = [talos_machine_configuration_apply.cp_config_apply]
  client_configuration = talos_machine_secrets.machine_secrets.client_configuration
  node                 = local.controlplane_1_ip
}

# data "talos_cluster_health" "health" {
#   depends_on           = [talos_machine_configuration_apply.cp_config_apply, talos_machine_configuration_apply.worker_config_apply]
#   client_configuration = data.talos_client_configuration.talosconfig.client_configuration
#   control_plane_nodes  = [local.controlplane_1_ip]
#   worker_nodes         = [local.worker_1_ip]
#   endpoints            = data.talos_client_configuration.talosconfig.endpoints
# }

resource "talos_cluster_kubeconfig" "kubeconfig" {
  depends_on           = [talos_machine_bootstrap.bootstrap] #, data.talos_cluster_health.health]
  client_configuration = talos_machine_secrets.machine_secrets.client_configuration
  node                 = local.controlplane_1_ip
}

resource "proxmox_virtual_environment_vm" "talos_controlplane_1" {
  name        = "talos-controlplane-1"
  description = "Managed by Terraform"
  tags        = ["terraform", "talos", "kubernetes"]

  vm_id     = 366
  node_name = local.node_name

  operating_system {
    type = "l26"
  }

  agent {
    enabled = true
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


  }

  cpu {
    # type = "host"
    type = "x86-64-v2-AES"
    sockets = 1
    cores   = 4
  }

  memory {
    dedicated = 6200
  }
  started         = true
  on_boot         = true
  stop_on_destroy = true

  disk {
    datastore_id = local.datastore_id
    file_id      = proxmox_virtual_environment_download_file.talos_1_9_3.id
    interface    = "virtio0"
    file_format  = "raw"
    size         = 60
  }
  network_device {
    bridge = "vmbr0"
  }

  lifecycle {
    ignore_changes = [
      started,
      disk[0].file_id
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


resource "proxmox_virtual_environment_vm" "talos_worker" {
  depends_on = [ proxmox_virtual_environment_vm.talos_controlplane_1 ]
  for_each = {
    for index, i in local.worker_ips :
    index => i
  }
  name        = "talos-worker-${sum([each.key, 1])}"
  description = "Managed by Terraform"
  tags        = ["terraform", "talos", "kubernetes"]

  vm_id     = sum([each.key, 369])
  node_name = local.node_name
  # bios      = "ovmf"
  # machine   = "q35"

  operating_system {
    type = "l26"
  }



  agent {
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
        address = "${each.value}/24"
        gateway = "10.0.40.1"
      }
    }

    dns {
      servers = ["10.0.40.4", "10.0.40.1"]
      domain  = "home.mndy.be"
    }
  }

  cpu {
    # type = "host"
    type = "x86-64-v2-AES"
    sockets = 1
    cores   = 5
  }

  memory {
    dedicated = 9000
  }
  started         = true
  on_boot         = true
  stop_on_destroy = true

  disk {
    datastore_id = local.datastore_id
    file_id      = proxmox_virtual_environment_download_file.talos_1_9_3.id
    interface    = "virtio0"
    file_format  = "raw"
    size         = 60
  }
  network_device {
    bridge = "vmbr0"
  }

  lifecycle {
    ignore_changes = [
      started,
      # initialization[0].user_data_file_id,
      initialization[0],
      disk[0].file_id
    ]
  }
  # provisioner "local-exec" {
  #   when = destroy
  #   # TODO: what is with the weird 7th index thing here...
  #   # command = "set -x; talosctl reset -n ${try(self.ipv4_addresses[7][0])} --wait && kubectl delete node --wait talos-worker-${sum([each.key, 1])}"
  #   interpreter = ["bash", "-c"]
  # }
}



