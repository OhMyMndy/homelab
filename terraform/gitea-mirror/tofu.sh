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

# TODO: get github token from bw

if [[ "$GITHUB_TOKEN" != '' ]]; then
  echo "github_token = \"$GITHUB_TOKEN\"" >>terraform.tfvars
fi

exec tofu "$@"
