resource "proxmox_virtual_environment_vm" "tailscale-subnet-router" {
  name        = "tailscale-subnet-router"
  description = "Managed by Terraform"
  tags        = ["terraform", "ubuntu", "tailscale"]


  vm_id = 600

  node_name = local.node_name

  operating_system {
    type = "l26"
  }

  agent {
    enabled = true
  }

  initialization {
    datastore_id = local.datastore_id
    ip_config {
      ipv4 {
        address = "dhcp"
      }
    }
    # ip_config {
    #   ipv4 {
    #     address = "10.0.40.30/24"
    #     gateway = "10.0.40.1"
    #   }
    # }

    # dns {
    #   servers = ["10.0.40.4", "10.0.40.1"]
    #   domain = "home.mndy.be"
    # }
    user_data_file_id = proxmox_virtual_environment_file.tailscale-subnet-router.id
  }

  cpu {
    type    = "EPYC-IBPB"
    sockets = 1
    cores   = 1
    limit   = 64
  }

  memory {
    dedicated = 512
  }
  started         = true
  on_boot         = true
  stop_on_destroy = true

  disk {
    datastore_id = local.datastore_id
    file_id      = proxmox_virtual_environment_download_file.ubuntu_24_04.id
    interface    = "virtio0"
    file_format  = "raw"
    size         = 30
  }
  network_device {
    bridge = "vmbr0"
  }

  lifecycle {
    ignore_changes = [
      started,
      disk[0].file_id,
      initialization[0].user_data_file_id
    ]
  }

}

resource "proxmox_virtual_environment_file" "tailscale-subnet-router" {
  content_type = "snippets"
  datastore_id = "shared-nfs"
  node_name    = local.node_name
  overwrite    = true

  source_raw {
    data      = <<-EOD
    #cloud-config
    hostname: tailscale-subnet-router
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
        - apt-get install -y qemu-guest-agent net-tools
        - timedatectl set-timezone Europe/Brussels
        - systemctl enable qemu-guest-agent
        - systemctl start qemu-guest-agent

        - curl -fsSL https://tailscale.com/install.sh | sh
        - echo "net.ipv4.ip_forward = 1" > /etc/sysctl.d/tailscale.conf
        - sysctl --system
        - |
          cat <<EOF | sudo tee  /etc/NetworkManager/dispatcher.d/50-tailscale >/dev/null
          #!/usr/bin/env bash

          if [[ "$DEVICE_IFACE" = "tailscale0" ]]; then
            ip route del 10.0.40.0/24 dev tailscale0 table 52
          fi
          EOF

        - tailscale up --auth-key "${var.tailscale_auth_key}" --accept-routes --advertise-routes 10.0.40.0/24 --advertise-exit-node
        - echo "done" > /tmp/cloud-config.done
    EOD
    file_name = "tailscale-subnet-router-cloud-config.yaml"

  }
}
