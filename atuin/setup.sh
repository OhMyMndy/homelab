#!/usr/bin/env bash

set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR" || exit 1

source ../deploy/functions.sh

if [[ ! -f .env ]] && [[ -f env-example ]]; then
  cp env-example .env
fi

add_to_env ATUIN_DB_NAME atuin
add_to_env ATUIN_DB_USERNAME atuin
add_to_env ATUIN_DB_PASSWORD "$(random_password)"

create_host_dirs
