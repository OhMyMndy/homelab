#!/usr/bin/env bash

set -eu

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR" || exit 1

source ../deploy/functions.sh

# source ../lldap/.env
# add_to_env LLDAP_LDAP_USER_PASS "${LLDAP_LDAP_USER_PASS}"

add_to_env OPENAI_API_BASE_URL "https://litellm.home.ohmymndy.com/"

(
  source ../litellm/.env
  add_to_env_force OPENAI_API_KEY "$LITELLM_API_KEY"
)
add_to_env ENABLE_LDAP "True"
add_to_env LDAP_APP_DN "uid=admin,ou=people,dc=ohmymndy,dc=com"
(
  source ../lldap/.env
  add_to_env_force LDAP_APP_PASSWORD "$LLDAP_LDAP_USER_PASS"
)
add_to_env_force LDAP_ATTRIBUTE_FOR_USERNAME uid
add_to_env_force LDAP_SEARCH_BASE "ou=people,dc=ohmymndy,dc=com"
# add_to_env_force LDAP_SEARCH_FILTERS "(&(objectClass=person)(|(uid=%s)(mail=%s)))"
add_to_env_force LDAP_SERVER_HOST lldap
add_to_env_force LDAP_SERVER_PORT 3890
add_to_env_force LDAP_USE_TLS "False"

create_host_dirs
