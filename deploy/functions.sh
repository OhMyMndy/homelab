#!/usr/bin/env bash

FUNCTIONS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [[ -f "$FUNCTIONS_DIR/../.bw-login" ]]; then
  BW_SESSION="$(cat "$FUNCTIONS_DIR/../.bw-login")"
  export BW_SESSION
fi

export TAILSCALE_IP
export LOCAL_IP

TAILSCALE_IP="$(ip -f inet addr show tailscale0 2>/dev/null | sed -En -e 's/.*inet ([0-9.]+).*/\1/p')"
LOCAL_IP="$(ip addr show ens18 2>/dev/null | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' -m 1 | head -1)"

export PUID
export PGID

export TIMEZONE

PUID="$(id -u)"
PGID="$(id -g)"
TIMEZONE=Europe/Brussels

# if ! command -v jq &>/dev/null; then
#   echo "jq not found..." 1>&2
# fi
#
# if ! command -v yq &>/dev/null; then
#   echo "yq not found..." 1>&2
# fi
#
# if ! command -v openssl &>/dev/null; then
#   echo "openssl not found..." 1>&2
# fi

function start() {
  local stacks="$*"

  for stack in $stacks; do
    echo "Deploying stack: $stack"

    (
      cd "$stack" &&
        if [[ -f ./setup.sh ]]; then ./setup.sh; fi &&
        docker compose up -d --remove-orphans --build
    )
  done
}

function add_to_env_force() {
  local key="$1"
  local value="$2"
  local filename="${3:-.env}"
  touch "${filename}"
  sed -E -i "/^${key}=/d" "${filename}"
  echo "${key}=${value}" >>"${filename}"
}

function add_tfvars_force() {
  local key="$1"
  local value="$2"
  local file="$3"
  touch "$file"
  sed -E -i "/^${key}\s*=/d" "$file"
  # TODO: escape $value
  echo "${key} = \"${value}\"" >>"$file"
}

function add_to_env() {
  local key="$1"
  local value="$2"
  local filename="${3:-.env}"
  touch "${filename}"
  if ! grep -q "${key}=" "${filename}"; then
    echo "${key}=${value}" >>"${filename}"
  fi
}

function random_password() {
  local length="${1:-38}"
  openssl rand -base64 $length | tr -dc 'a-zA-Z0-9' | tr -d '\n'
}

function create_host_dirs() {
  docker compose config | yq '.services[].volumes[].source' | grep "^$PWD" | tr '\n' '\0' |
    xargs -0 -r -I{} bash -c "source=\"{}\"; if [[ ! \"\$source\" == *.* ]]; then mkdir -p \"\$source\"; chmod 777 \"\$source\"; fi"
}
