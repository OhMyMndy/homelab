#!/usr/bin/env bash

export TAILSCALE_IP
export LOCAL_IP

TAILSCALE_IP="$(ip -f inet addr show tailscale0 | sed -En -e 's/.*inet ([0-9.]+).*/\1/p')"
LOCAL_IP="$(ip addr show ens18 | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' -m 1 | head -1)"

export PUID
export PGID

export AUTHENTIK_TAG=2

export TIMEZONE

PUID="$(id -u)"
PGID="$(id -g)"
TIMEZONE=Europe/Brussels

function start() {
  local stacks="$*"

  for stack in $stacks; do
    echo "Deploying stack: $stack"

    (cd "$stack" && docker compose up -d --remove-orphans --build)
  done
}
