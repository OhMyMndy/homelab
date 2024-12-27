#!/usr/bin/env bash

export TAILSCALE_IP
export LOCAL_IP

TAILSCALE_IP="$(ip -f inet addr show tailscale0 | sed -En -e 's/.*inet ([0-9.]+).*/\1/p')"
LOCAL_IP="$(ip addr show ens18 | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' -m 1 | head -1)"

export PUID
export PGID

export TIMEZONE

PUID="$(id -u)"
PGID="$(id -g)"
TIMEZONE=Europe/Brussels

if ! command -v jq &>/dev/null; then
  echo "jq not found..." 1>&2
fi

if ! command -v yq &>/dev/null; then
  echo "yq not found..." 1>&2
fi

if ! command -v openssl &>/dev/null; then
  echo "openssl not found..." 1>&2
fi

function start() {
  local stacks="$*"

  for stack in $stacks; do
    echo "Deploying stack: $stack"

    (cd "$stack" && docker compose up -d --remove-orphans --build)
  done
}

function add_to_env() {
  local key="$1"
  local value="$2"
  if ! grep -q "${key}=" .env; then
    echo "${key}=${value}" >>.env
  fi
}

function random_password() {
  openssl rand -base64 38 | tr -d '\n'
}

function create_host_dirs() {
  docker compose config | yq '.services[].volumes[].source' | grep "^$PWD" | tr '\n' '\0' | xargs -0 -r -I{} bash -c "mkdir -p {}"
}
