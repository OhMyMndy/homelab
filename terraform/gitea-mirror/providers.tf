terraform {
  required_providers {
    gitea = {
      source  = "registry.terraform.io/go-gitea/gitea"
      version = "0.5.2"
    }
  }
}

provider "gitea" {
  base_url = var.gitea_url
  # token    = var.gitea_token
}
