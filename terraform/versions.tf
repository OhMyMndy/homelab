terraform {
  required_providers {
    proxmox = {
      source  = "bpg/proxmox"
      version = "0.70.1"
    }
    talos = {
      source  = "siderolabs/talos"
      version = "0.7.1"
    }
    random = {
      source  = "hashicorp/random"
      version = "3.6.3"
    }
    tls = {
      source  = "hashicorp/tls"
      version = "4.0.6"
    }
    null = {
      source  = "hashicorp/null"
      version = "3.2.3"
    }
    archive = {
      source  = "hashicorp/archive"
      version = "2.6.0"
    }
  }
}
