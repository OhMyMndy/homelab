terraform {
  required_version = ">= 0.13"

  required_providers {
    proxmox = {
      source  = "bpg/proxmox"
      version = ">=0.73.0"
    }
  }
}


resource "proxmox_virtual_environment_vm" "this" {
  name        = var.hostname
  description = "Managed by Terraform"
  tags        = var.tags

  timeout_create = 240
  timeout_start_vm = 240
  timeout_clone = 240
  vm_id = var.vm_id

  node_name = var.node_name

  operating_system {
    type = "l26"
  }

  agent {
    enabled = true
  }

  initialization {
    datastore_id = var.datastore_id

    # DHCP when we do not specify an IP address
    dynamic "ip_config" {
      for_each = var.ip_address == null ? [1] : []
      content {
        ipv4 {
          address = "dhcp"
        }
      }
    }

    # Static IP when we specify an IP address
    dynamic "ip_config" {
      for_each = var.ip_address != null ? [var.ip_address] : []
      content {
        ipv4 {
          address = var.ip_address
          gateway = "10.0.40.1"
        }
      }
    }

    # Set DNS when we specify an IP address
    dynamic "dns" {
      for_each = var.ip_address != null ? [var.ip_address] : []
      content {
        servers = ["10.0.40.4", "10.0.40.1"]
        domain  = "home.mndy.be"
      }
    }


    user_data_file_id = proxmox_virtual_environment_file.this.id
  }

  cpu {
    type    = var.cpu_type
    sockets = 1
    cores   = var.cores
    limit   = var.cpu_limit
  }

  memory {
    dedicated = var.memory
  }
  started         = true
  on_boot         = var.on_boot
  stop_on_destroy = true

  disk {
    datastore_id = var.datastore_id
    file_id      = var.image
    interface    = "virtio0"
    file_format  = "raw"
    size         = var.disk_size
  }


  network_device {
    bridge = "vmbr0"
  }

  lifecycle {
    ignore_changes = [
      started,
      disk[0].file_id,
    ]
  }

}


resource "proxmox_virtual_environment_file" "this" {
  content_type = "snippets"
  datastore_id = var.snippets_datastore_id
  node_name    = var.node_name
  overwrite    = true

  source_raw {
    data = var.cloud_init
    # <<-EOF
    # #cloud-config
    # hostname: tailscale-subnet-router
    # users:
    #   - name: mandy
    #     groups:
    #       - sudo
    #     shell: /bin/bash
    #     ssh_authorized_keys:
    #       - ${trimspace(data.local_file.ssh_public_key.content)}
    #     sudo: ALL=(ALL) NOPASSWD:ALL
    # runcmd:
    #     - apt update
    #     - apt-get install -y qemu-guest-agent net-tools
    #     - timedatectl set-timezone Europe/Brussels
    #     - systemctl enable qemu-guest-agent
    #     - systemctl start qemu-guest-agent
    #
    #     - curl -fsSL https://tailscale.com/install.sh | sh
    #     - echo "net.ipv4.ip_forward = 1" > /etc/sysctl.d/tailscale.conf
    #     - sysctl --system
    #
    #     - tailscale up --auth-key "${var.tailscale_auth_key}" --accept-routes --advertise-routes 10.0.40.0/24 --advertise-exit-node
    #     - echo "done" > /tmp/cloud-config.done
    # EOF
    file_name = "${var.hostname}-cloud-config.yaml"

  }
}
