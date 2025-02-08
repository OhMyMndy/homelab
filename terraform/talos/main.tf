provider "proxmox" {
  endpoint = var.proxmox_endpoint
  insecure = true

  ssh {
    agent = true
  }

  # timeout {
  #   create = "20m"
  # }
}
