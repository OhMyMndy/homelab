#!/usr/bin/env bash


DIR="$(dirname "$(readlink -f "$0")")"

cd "$DIR"

mkdir -p "$HOME/Obsidian"

docker compose up -d --remove-orphans
