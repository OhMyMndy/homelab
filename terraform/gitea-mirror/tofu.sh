#!/usr/bin/env bash

set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR" || exit 1

source ../../deploy/functions.sh

source ../../gitea-mirror/.env

GITEA_BASE_URL=https://gitea-mirror.home.ohmymndy.com

echo "gitea_url = \"$GITEA_BASE_URL\"" >terraform.tfvars
export GITEA_USERNAME=ohmymndy-admin

source ../../lldap/.env

export GITEA_PASSWORD=${ADMIN_PASSWORD}

# stop if cannot unlock
bw unlock --check
GITHUB_TOKEN="$(bw get item 37e47220-bbc7-48bb-b39d-2679fb9c3cce |
  jq '.fields[] | select(.name =="public-repositories pat") | .value' -r)"

if [[ "$GITHUB_TOKEN" != '' ]]; then
  add_tfvars_force github_token "$GITHUB_TOKEN" terraform.tfvars
fi

exec tofu "$@"
