module "kasm" {
  source = "./modules/vm"
  count = 0

  hostname = "kasm-1"
  tags     = ["terraform", "ubuntu", "kasm"]

  vm_id = 500

  node_name             = local.node_name
  datastore_id          = local.datastore_id
  snippets_datastore_id = local.snippets_datastore_id
  ip_address            = "10.0.40.30/24"
  cores                 = 3
  memory                = 17000
  on_boot               = true
  disk_size             = 200

  image = proxmox_virtual_environment_download_file.ubuntu_24_04.id

  cloud_init = <<-EOF
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
        - apt-get install -y -q qemu-guest-agent net-tools
        - timedatectl set-timezone Europe/Brussels
        - systemctl enable qemu-guest-agent
        - systemctl start qemu-guest-agent

        # Necessary for Redroid for example
        - apt-get install -y -q linux-modules-extra-`uname -r`
        - echo 'binder_linux' > /etc/modules-load.d/binder_linux.conf
        - echo 'options binder_linux devices=binder,hwbinder,vndbinder' > /etc/modprobe.d/binder_linux.conf

        - mkdir -p /etc/docker
        - |
            echo '{ "registry-mirrors": ["https://oci.nexus.home.ohmymndy.com"] }' >/etc/docker/daemon.json
        - mkdir -p /tmp
        - cd /tmp
        - curl -O https://kasm-static-content.s3.amazonaws.com/kasm_release_1.16.1.98d6fa.tar.gz
        - tar -xf kasm_release_1.16.1.98d6fa.tar.gz
        - |
          set -x;
          bash kasm_release/install.sh --no-check-disk --no-check-ports --accept-eula --swap-size 6000 \
            --user-password "${var.kasm_user_password}" --admin-password "${var.kasm_admin_password}"
        - rm -rf kasm*
        - echo "done" > /tmp/cloud-config.done
    EOF
}
