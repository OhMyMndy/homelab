#!/usr/bin/env bash


DIR="$(dirname "$(readlink -f "$0")")"

cd "$DIR"

docker compose up -d --remove-orphans
