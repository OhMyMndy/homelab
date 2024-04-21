#!/usr/bin/env bash

DIR="$(dirname "$(readlink -f "$0")")/../"

cd "$DIR" || exit

source deploy/functions.sh


(cd reverse-proxy && docker-compose stop)

find . -maxdepth 1 -type d \! -name backups \! -name deploy \! -name '.*' -print0 | xargs -I{} -0 bash -c "cd {} && docker compose stop"