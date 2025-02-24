#!/usr/bin/env bash

set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR" || exit 1

source ../deploy/functions.sh

if [[ ! -f .env ]] && [[ -f env-example ]]; then
  cp env-example .env
fi
add_to_env BITWARDEN_ADMIN_TOKEN "$(random_password)"
create_host_dirs
