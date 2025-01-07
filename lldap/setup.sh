#!/usr/bin/env bash

set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR" || exit 1

source ../deploy/functions.sh

if [[ ! -f .env ]] && [[ -f env-example ]]; then
  cp env-example .env
fi

add_to_env LLDAP_JWT_SECRET "$(random_password)"
add_to_env LLDAP_KEY_SEED "$(random_password)$(random_password)"
add_to_env LLDAP_LDAP_USER_PASS "$(random_password)"

create_host_dirs
