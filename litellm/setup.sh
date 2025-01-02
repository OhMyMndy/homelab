#!/usr/bin/env bash

set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR" || exit 1

source ../deploy/functions.sh

add_to_env POSTGRES_DB litellm
add_to_env POSTGRES_USER litellm
add_to_env POSTGRES_PASSWORD "$(random_password)"
# source ../lldap/.env
# add_to_env LLDAP_LDAP_USER_PASS "${LLDAP_LDAP_USER_PASS}"

add_to_env LITELLM_MASTER_KEY "$(random_password)"
add_to_env LITELLM_SALT_KEY "$(random_password)"

# add_to_env OPEN_API_BASE_URL "https://litellm.home.ohmymndy.com/"

bw unlock --check
OPENROUTER_API_KEY="$(bw get item bde90fed-9d93-4f68-a541-c55528fa28d3 |
  jq '.fields[] | select(.name == "API KEY") | .value' -r)"

if [[ "$OPENROUTER_API_KEY" != '' ]]; then
  add_to_env_force OPENROUTER_API_KEY "$OPENROUTER_API_KEY"
fi

(
  source .env
  cd ../openwebui/
  add_to_env "# OPENAI_API_KEY is the API key for litellm" ''
  add_to_env_force "OPENAI_API_KEY" "$LITELLM_API_KEY"
)

create_host_dirs
