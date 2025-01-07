#!/usr/bin/env bash

set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR" || exit 1

source ../deploy/functions.sh

if [[ ! -f .env ]]; then
  cp env-example .env
fi

add_to_env POSTGRES_PASSWORD "$(random_password)"
add_to_env POSTGRES_USER redmine
add_to_env POSTGRES_DB redmine

create_host_dirs
