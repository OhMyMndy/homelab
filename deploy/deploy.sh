#!/usr/bin/env bash


DIR="$(dirname "$(readlink -f "$0")")/../"

cd "$DIR"

export TAILSCALE_IP

TAILSCALE_IP="$(ip -f inet addr show tailscale0 | sed -En -e 's/.*inet ([0-9.]+).*/\1/p')"

(cd reverse-proxy && docker-compose up -d)

(cd tt-rss && docker-compose up -d)

(cd vaultwarden && docker-compose up -d)

# (cd minecraft-bedrock-server && docker-compose up -d)

(cd firefly && docker-compose up -d)

(cd dashy && docker-compose up -d) 

( cd authentik;
if [[ ! -f .env ]]; then
    echo "PG_PASS=$(openssl rand -base64 36)" >> .env;
    echo "AUTHENTIK_SECRET_KEY=$(openssl rand -base64 36)" >> .env;
fi;
docker-compose up -d --remove-orphans
)