#!/usr/bin/env bash

set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR" || exit 1

BASE_URL="http://litellm:4000"

source ../deploy/functions.sh

source .env
if [[ "$LITELLM_API_KEY" == "" ]]; then
  echo "Creating Litellm api key"
  data="$(curl -s --location "${BASE_URL}/key/generate" \
    -H "Authorization: Bearer ${LITELLM_MASTER_KEY}" \
    -H 'Content-Type: application/json' --data '{}' | jq -r .key)"
  add_to_env_force LITELLM_API_KEY "$data"
fi

# TODO: import pipeline to add user to request to litellm

exit
curl --location "${BASE_URL}/budget/list" \
  -H "Authorization: Bearer ${LITELLM_MASTER_KEY}" \
  -H 'Content-Type: application/json' | jq

curl --location "${BASE_URL}/end_user/list" \
  -H "Authorization: Bearer ${LITELLM_MASTER_KEY}" \
  -H 'Content-Type: application/json' | jq

curl -X POST --location "${BASE_URL}/end_user/new" \
  -H "Authorization: Bearer ${LITELLM_MASTER_KEY}" \
  -H 'Content-Type: application/json' \
  -d '{"user_id": "mandyschoep@gmail.com", "budget_id": "mandy"}' | jq

curl -X POST --location "${BASE_URL}/end_user/new" \
  -H "Authorization: Bearer ${LITELLM_MASTER_KEY}" \
  -H 'Content-Type: application/json' \
  -d '{"user_id": "mandyschoep@gmail.com", "budget_id": "mandy"}' | jq

curl -X POST --location "${BASE_URL}/end_user/new" \
  -H "Authorization: Bearer ${LITELLM_MASTER_KEY}" \
  -H 'Content-Type: application/json' \
  -d '{"user_id": "riley.verhoeven93@gmail.com", "budget_id": "riley"}' | jq
