locals {
  # https://github.com/hashicorp/terraform-plugin-sdk
  mirrors = {
    "docker-compose-linter" : {
      name              = "docker-compose-linter",
      description       = "Docker Compose Linter",
      address           = "https://github.com/zavoloklom/docker-compose-linter.git",
      migration_service = "github",
    },

    "niki-on-github/nixos-k3s" : {
      name              = "niki-on-github-nixos-k3s",
      description       = "My NixOS based single node K3S Cluster using gitops (flux) and renovate automation fully reproducibly setup with a single command",
      address           = "https://github.com/niki-on-github/nixos-k3s.git",
      migration_service = "github",
    }
  }
}

resource "gitea_org" "ohmymndy-mirror" {
  name = "ohmymndy-mirror"
}

data "gitea_user" "ohmymndy" {
  username = "ohmymndy"
}

# resource "gitea_team" "mirror" {
#   name         = "Mirror"
#   organisation = gitea_org.ohmymndy-mirror.name
#   description  = "Mirror team"
#   permission   = "write"
# }
#
# resource "gitea_team_members" "mirror" {
#   team_id = gitea_team.mirror.id
#   members = [data.gitea_user.ohmymndy.username]
# }

# resource "gitea_repository" "mirror" {
#   for_each                     = local.mirrors
#   username                     = gitea_org.ohmymndy-mirror.name
#   name                         = each.value.name
#   description                  = each.value.description
#   mirror                       = true
#   migration_clone_address      = each.value.address
#   migration_service            = each.value.migration_service
#   migration_releases           = true
#   migration_mirror_interval    = "24h"
#   migration_service_auth_token = var.github_token
# }
