variable "proxmox_endpoint" {
  type = string
}

variable "proxmox_username" {
  type = string
}

variable "proxmox_api_token" {
  type      = string
  sensitive = true
}

variable "tailscale_auth_key" {
  type      = string
  sensitive = true
}

variable "kasm_user_password" {
  type      = string
  sensitive = true
}

variable "kasm_admin_password" {
  type      = string
  sensitive = true
}

