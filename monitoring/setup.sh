#!/usr/bin/env bash

set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR" || exit 1

source ../deploy/functions.sh

source ../lldap/.env

add_to_env_force GF_LDAP_PORT 3890
add_to_env_force GF_LDAP_HOST lldap

add_to_env_force GF_LDAP_USER "uid=admin_ro,ou=people,dc=ohmymndy,dc=com"
add_to_env_force GF_LDAP_PASS "${ADMIN_RO_PASSWORD}"

add_to_env GF_RENDERING_RENDERER_TOKEN "$(openssl rand -base64 32 | tr -dc 'a-zA-Z0-9' | tr -d '\n')"

LOKI_AUTH="$(openssl rand -base64 32 | tr -dc 'a-zA-Z0-9' | tr -d '\n')"
add_to_env LOKI_PASS "$LOKI_AUTH"

LOKI_AUTH="$(htpasswd -nbB loki "$LOKI_AUTH")"
LOKI_AUTH="${LOKI_AUTH//$/\\$}"
add_to_env LOKI_AUTH "$LOKI_AUTH"

set -x
PROMETHEUS_AUTH="$(openssl rand -base64 32 | tr -dc 'a-zA-Z0-9' | tr -d '\n')"
add_to_env PROMETHEUS_PASS "$PROMETHEUS_AUTH"

PROMETHEUS_AUTH="$(htpasswd -nbB prometheus "$PROMETHEUS_AUTH")"
PROMETHEUS_AUTH="${PROMETHEUS_AUTH//$/\\$}"
add_to_env PROMETHEUS_AUTH "$PROMETHEUS_AUTH"

add_to_env_force HOST_HOSTNAME "$(hostname)"
set +x
create_host_dirs || true

#uid 472 grafana
