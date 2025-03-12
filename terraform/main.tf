locals {
  node_name             = "pve-2"
  datastore_id          = "local-zfs"
  snippets_datastore_id = "shared-nfs"
}

provider "proxmox" {
  endpoint = var.proxmox_endpoint
  insecure = true
  # username = var.proxmox_username
  api_token = var.proxmox_api_token
  ssh {
    agent    = true
    username = var.proxmox_username
  }
}

data "local_file" "ssh_public_key" {
  filename = "/home/mandy/.ssh/id_ed25519.pub"
}