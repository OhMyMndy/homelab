#!/usr/bin/env bash

set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR" || exit 1

source ../deploy/functions.sh

add_to_env MINIO_ROOT_USER root
add_to_env MINIO_ROOT_PASSWORD "$(random_password)"

add_to_env MINIO_TERRAFORM_USER terraform
add_to_env MINIO_TERRAFORM_PASSWORD "$(random_password)"


create_host_dirs
