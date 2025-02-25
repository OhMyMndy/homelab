#!/usr/bin/env bash

set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR" || exit 1

source ../deploy/functions.sh

add_to_env POSTGRES_PASSWORD "$(random_password)"
add_to_env POSTGRES_USER postgres
add_to_env POSTGRES_DB luminus-dynamic-api

create_host_dirs
