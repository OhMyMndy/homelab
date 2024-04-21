#!/usr/bin/env bash

DIR="$(dirname "$(readlink -f "$0")")/../"

cd "$DIR" || exit

source deploy/functions.sh

deploy/stop.sh


# date command to get d-m-y H:i:s
date=$(date +"%d-%m-%Y-%H:%M:%S")


mkdir -p backups

sudo tar --exclude='deploy' --exclude='backups' -czf "backups/backup-homelab-${date}.tar.gz" .
sudo chown "$(id -u):$(id -g)" "backups/backup-homelab-${date}.tar.gz"
