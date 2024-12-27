#!/usr/bin/env bash

set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR" || exit 1

source ../deploy/functions.sh

if [[ ! -f .env ]]; then
  cp env-example .env
fi

add_to_env POSTGRES_PASSWORD "$(random_password)"
add_to_env POSTGRES_USER n8n
add_to_env POSTGRES_DB n8n

add_to_env N8N_ENCRYPTION_KEY "$(random_password)$(random_password)"
add_to_env N8N_USER_MANAGEMENT_JWT_SECRET "$(random_password)"

create_host_dirs
