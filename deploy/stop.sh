#!/usr/bin/env bash


DIR="$(dirname "$(readlink -f "$0")")/../"

cd "$DIR"


(cd reverse-proxy && docker-compose stop)

(cd tt-rss && docker-compose stop)

(cd vaultwarden && docker-compose stop)

# (cd minecraft-bedrock-server && docker-compose stop)

(cd firefly && docker-compose stop)

(cd dashy && docker-compose stop)

(cd adguard && docker-compose stop)