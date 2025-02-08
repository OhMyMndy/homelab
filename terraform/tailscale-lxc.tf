resource "proxmox_virtual_environment_container" "tailscale" {
  description = "Tailscale LXC Container"

  node_name = "pve-1"
  vm_id     = 8000

  initialization {
    hostname = "tailscale"

    ip_config {
      ipv4 {
        address = "dhcp"
      }
    }

    user_account {
      keys = [
        trimspace(tls_private_key.ubuntu_container_key.public_key_openssh)
      ]
      password = random_password.ubuntu_container_password.result
    }
  }

  network_interface {
    name = "veth0"
  }

  operating_system {
    template_file_id = proxmox_virtual_environment_download_file.ubuntu_noble_lxc.id
    type             = "ubuntu"
  }

  disk {
    datastore_id = "local"
    size         = 4
  }

  memory {
    dedicated = 512
    swap      = 0
  }

  started       = true
  start_on_boot = true
  startup {
    order = "3"
    # up_delay   = "60"
    # down_delay = "60"
  }
  unprivileged = true

  hook_script_file_id = proxmox_virtual_environment_file.hook_script.id
}

# to test: /var/lib/vz/snippets/tailscale-pre-start.sh 8000 pre-start
resource "proxmox_virtual_environment_file" "hook_script" {
  content_type = "snippets"
  datastore_id = "local"
  node_name    = "pve-1"
  # Hook scripts must be executable, otherwise the Proxmox VE API will reject the configuration for the VM/CT.
  file_mode = "0700"

  source_raw {
    data      = file("./tailscale-pre-start.sh")
    file_name = "tailscale-pre-start.sh"
  }
}

resource "random_password" "ubuntu_container_password" {
  length           = 16
  override_special = "_%@"
  special          = true
}

resource "tls_private_key" "ubuntu_container_key" {
  algorithm = "RSA"
  rsa_bits  = 2048
}

output "ubuntu_container_password" {
  value     = nonsensitive(random_password.ubuntu_container_password.result)
  sensitive = false
}

output "ubuntu_container_private_key" {
  value     = tls_private_key.ubuntu_container_key.private_key_pem
  sensitive = true
}

output "ubuntu_container_public_key" {
  value = tls_private_key.ubuntu_container_key.public_key_openssh
}

# resource "null_resource" "" {
#
# }
