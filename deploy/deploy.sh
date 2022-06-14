#!/usr/bin/env bash


DIR="$(dirname "$(readlink -f "$0")")/../"

cd "$DIR"


(cd reverse-proxy && docker compose up -d)

(cd rclone && ./deploy.sh)

(cd tt-rss && docker compose up -d)

(cd vaultwarden && docker compose up -d)


(cd obsidian && ./deploy.sh)

(cd minecraft-bedrock-server && docker compose up -d)
