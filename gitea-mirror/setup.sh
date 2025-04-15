#!/usr/bin/env bash

set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR" || exit 1

source ../deploy/functions.sh

add_to_env POSTGRES_DB gitea
add_to_env POSTGRES_USER gitea
add_to_env POSTGRES_PASSWORD "$(random_password)"
add_to_env GITEA_SECRET_KEY "$(docker run -it --rm docker.io/gitea/gitea:1 gitea generate secret SECRET_KEY)"
add_to_env GITEA_INTERNAL_TOKEN "$(docker run -it --rm docker.io/gitea/gitea:1 gitea generate secret INTERNAL_TOKEN)"

source ../lldap/.env

add_to_env_force LLDAP_LDAP_USER_PASS "${ADMIN_RO_PASSWORD}"

create_host_dirs
