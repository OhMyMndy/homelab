#!/usr/bin/env bash

set -e
DIR="$(dirname "$(readlink -f "$0")")"

cd "$DIR" || exit

docker compose exec -it postgresql ash -c 'PGPASSWORD=$POSTGRESS_PASSWORD pg_dump -Fc -U $POSTGRES_USER' > "backups/backup-$(date "+%F-%H-%M-%S")"

docker compose exec -it postgresql ash -c 'PGPASSWORD=$POSTGRESS_PASSWORD pg_dumpall --globals-only -U $POSTGRES_USER' > "backups/backup-$(date "+%F-%H-%M-%S")-roles.sql"

