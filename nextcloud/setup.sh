#!/usr/bin/env bash

set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR" || exit 1

source ../deploy/functions.sh

add_to_env MYSQL_PASSWORD "$(random_password)"
add_to_env MYSQL_ROOT_PASSWORD "$(random_password)"

create_host_dirs
