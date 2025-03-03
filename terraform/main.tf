provider "proxmox" {
  endpoint = var.proxmox_endpoint
  insecure = true
  # username = var.proxmox_username
  api_token = var.proxmox_api_token
  ssh {
    agent = true
    username = var.proxmox_username
  }
}
