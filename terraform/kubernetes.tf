locals {
  node_name    = "pve-2"
  datastore_id = "local-zfs"

}

resource "proxmox_virtual_environment_vm" "ubuntu_24_04" {
  for_each = {
    "kubernetes-1" = {
      vm_id = 401,
      ip_address = "10.0.40.81/24"
    },
    "kubernetes-2" = {
      vm_id = 402,
      ip_address = "10.0.40.82/24"
    }
  }
  name        = "kubernetes-1"
  description = "Managed by Terraform"
  tags = ["terraform", "ubuntu", "kubernetes"]


  vm_id = each.value.vm_id

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
        address = each.value.ip_address
        gateway = "10.0.40.1"
      }
    }

    dns {
      servers = ["10.0.40.4", "10.0.40.1"]
      domain = "home.mndy.be"
    }
    user_data_file_id = proxmox_virtual_environment_file.kubernetes_user_data.id
  }

  cpu {
    type    = "EPYC-IBPB"
    sockets = 1
    cores   = 4
  }

  memory {
    dedicated = 20000
  }
  started         = true
  on_boot         = true
  stop_on_destroy = true

  disk {
    datastore_id = local.datastore_id
    file_id      = proxmox_virtual_environment_download_file.ubuntu_24_04.id
    interface    = "virtio0"
    file_format  = "raw"
    size         = 200
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

}

data "local_file" "ssh_public_key" {
  filename = "/home/mandy/.ssh/id_ed25519.pub"
}

resource "proxmox_virtual_environment_file" "kubernetes_user_data" {
  content_type = "snippets"
  datastore_id = "shared-nfs"
  node_name    = local.node_name
  overwrite    = true

  source_raw {
    data = <<-EOF
    #cloud-config
    hostname: kubernetes-1
    users:
      - name: mandy
        groups:
          - sudo
        shell: /bin/bash
        ssh_authorized_keys:
          - ${trimspace(data.local_file.ssh_public_key.content)}
        sudo: ALL=(ALL) NOPASSWD:ALL
    runcmd:
        - apt update
        - apt install -y qemu-guest-agent net-tools
        - timedatectl set-timezone Europe/Brussels
        - systemctl enable qemu-guest-agent
        - systemctl start qemu-guest-agent
        - echo "done" > /tmp/cloud-config.done
    EOF

    file_name = "user-data-cloud-config.yaml"
  }
}
