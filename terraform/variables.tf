variable "proxmox_endpoint" {
  type = string
}

variable "proxmox_username" {
  type = string
}

variable "proxmox_api_token" {
  type = string
  sensitive = true
}
