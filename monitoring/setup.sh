#!/usr/bin/env bash

set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR" || exit 1

source ../deploy/functions.sh

source ../lldap/.env

add_to_env_force GF_LDAP_PORT 3890
add_to_env_force GF_LDAP_HOST lldap

add_to_env_force GF_LDAP_USER "uid=admin,ou=people,dc=ohmymndy,dc=com"
add_to_env_force GF_LDAP_PASS "${LLDAP_LDAP_USER_PASS}"

create_host_dirs

#uid 472 grafana
