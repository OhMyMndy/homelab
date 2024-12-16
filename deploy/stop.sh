#!/usr/bin/env bash

DIR="$(dirname "$(readlink -f "$0")")/../"

cd "$DIR" || exit

(source deploy/functions.sh && cd reverse-proxy && docker compose down)

find . -maxdepth 1 -type d \! -name backups \! -name deploy \! -name '.*' -print0 |
  xargs -I{} -0 bash -c "source deploy/functions.sh && cd {} && docker compose down"
