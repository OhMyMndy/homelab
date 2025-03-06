resource "proxmox_virtual_environment_vm" "kasm" {
  name        = "kasm-1"
  description = "Managed by Terraform"
  tags = ["terraform", "ubuntu", "kasm"]


  vm_id = 500

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
        address = "10.0.40.30/24"
        gateway = "10.0.40.1"
      }
    }

    dns {
      servers = ["10.0.40.4", "10.0.40.1"]
      domain = "home.mndy.be"
    }
    user_data_file_id = proxmox_virtual_environment_file.kasm_user_data.id
  }

  cpu {
    type    = "EPYC-IBPB"
    sockets = 1
    cores   = 3
  }

  memory {
    dedicated = 17000
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
      disk[0].file_id,
      initialization[0].user_data_file_id
    ]
  }

}

resource "proxmox_virtual_environment_file" "kasm_user_data" {
  content_type = "snippets"
  datastore_id = "shared-nfs"
  node_name    = local.node_name
  overwrite    = true

  source_raw {
    data = <<-EOF
    #cloud-config
    hostname: kasm-1
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

        # Necessary for Redroid for example
        - apt-get install -y linux-modules-extra-`uname -r`
        - echo 'binder_linux' > /etc/modules-load.d/binder_linux.conf
        - echo 'options binder_linux devices=binder,hwbinder,vndbinder' > /etc/modprobe.d/binder_linux.conf

        - mkdir -p /etc/docker
        - |
            echo '{ "registry-mirrors": ["https://oci.nexus.home.ohmymndy.com"] }' >/etc/docker/daemon.json
        - mkdir -p /tmp
        - cd /tmp
        - curl -O https://kasm-static-content.s3.amazonaws.com/kasm_release_1.16.1.98d6fa.tar.gz
        - tar -xf kasm_release_1.16.1.98d6fa.tar.gz
        - bash kasm_release/install.sh --no-check-disk --no-check-ports --accept-eula --swap-size 6000
        - rm -rf kasm*
        - echo "done" > /tmp/cloud-config.done
    EOF

    file_name = "kasm-user-data-cloud-config.yaml"
  }
}
