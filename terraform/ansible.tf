data "archive_file" "ansible_archive" {
  type        = "zip"
  source_dir  = "ansible"
  output_path = "${path.module}/tmp/ansible.zip"
}

resource "null_resource" "ansible-inventory" {
  depends_on = [
    proxmox_virtual_environment_container.tailscale
  ]
  triggers = {
    always_run = "${timestamp()}" # data.archive_file.ansible_archive.output_sha256
  }
  provisioner "local-exec" {
    command = <<EOF
    if ! command -v ansible-playbook &>/dev/null; then
      echo "Ansible not installed" 1>&2
      exit 2
    fi
    MAC_ADDRESS="${proxmox_virtual_environment_container.tailscale.network_interface[0].mac_address}" 
    MAC_ADDRESS="$(echo "$MAC_ADDRESS" | tr '[:upper:]' '[:lower:]')"

    nmap -sP 10.0.40.0/24 >/dev/null
    IP_ADDRESS="$(arp -an | grep "$MAC_ADDRESS"| awk '{print $2}' | sed 's/[()]//g')"
    echo $IP_ADDRESS

    if [[ "$IP_ADDRESS" == "" ]]; then
      echo "Ip address not found..." 1>&2
      exit 3
    fi
    echo "${nonsensitive(tls_private_key.ubuntu_container_key.private_key_pem)}" >/tmp/private_key
    chmod 600 /tmp/private_key

    echo " 
    tailscale_subnet_router:
      hosts:
        $IP_ADDRESS:
          ansible_user: root
          ansible_ssh_private_key_file: /tmp/private_key
    " > ansible-inventory.yml

    # TODO: check if hosts are up
    ansible-galaxy install -r ansible/requirements.yml
    ansible-playbook \
        -i ansible-inventory.yml \
        ansible/tailscale.yml \
        --verbose \
        --ssh-common-args='-o StrictHostKeyChecking=no'

    rm /tmp/private_key
    EOF
  }
}
