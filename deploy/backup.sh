#!/usr/bin/env bash

set -e
DIR="$(dirname "$(readlink -f "$0")")/../"

cd "$DIR" || exit
set -x
source deploy/functions.sh

# ./deploy/stop.sh
sudo systemctl stop docker.socket docker.service

# date command to get d-m-y H:i:s
date=$(date +"%d-%m-%Y-%H_%M_%S")

DIR=/mnt/backups/homelab

sudo tar --exclude='deploy' \
  --exclude='audiobookshelf/storage/podcasts' \
  --exclude='kasm/storage' \
  --exclude='kiwix/storage' \
  --exclude='adguard/storage/work/data/querylog.json' \
  --exclude='streamrip/storage/Downloads' \
  --exclude='netbootxyz/assets' \
  --exclude='n8n/storage/ollama/models' \
  --exclude='plex/storage' \
  --exclude='backups' \
  --exclude='nexus/storage/nexus/blobs' \
  --exclude='pokeblahaj/storage/uploads' \
  -czf "$DIR/backup-homelab-${date}.tar.gz" .

#sudo chown "$(id -u):$(id -g)" "$DIR/backup-homelab-${date}.tar.gz"

sudo systemctl start docker.service
