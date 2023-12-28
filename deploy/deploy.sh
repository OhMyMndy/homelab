#!/usr/bin/env bash


DIR="$(dirname "$(readlink -f "$0")")/../"

cd "$DIR"


(cd reverse-proxy && docker-compose up -d)

(cd tt-rss && docker-compose up -d)

(cd vaultwarden && docker-compose up -d)

# (cd minecraft-bedrock-server && docker-compose up -d)

(cd firefly && docker-compose up -d)

(cd dashy && docker-compose up -d) 

(cd adguard && docker-compose up -d)
