#!/usr/bin/env bash
set -e
DIR="$(dirname "$(readlink -f "$0")")/../"

cd "$DIR" || exit

source deploy/functions.sh

(source .env-cloudflare && export CF_API_EMAIL CF_API_KEY &&
    nix run nixpkgs#flarectl -- dns create-or-update --zone ohmymndy.com --name '*.home-tailscale' --content $TAILSCALE_IP --type A) || true

(source .env-cloudflare && export CF_API_EMAIL CF_API_KEY &&
    nix run nixpkgs#flarectl -- dns create-or-update --zone ohmymndy.com --name '*.home' --content $LOCAL_IP --type A) || true

start reverse-proxy lldap adguard smtprelay status vaultwarden authentik dashy homepage wallabag \
    redmine tt-rss humblebundle-downloader searxng \
    gitea-mirror \
    kiwix pokeblahaj \
    litellm openwebui n8n

(source .env-cloudflare && export CF_API_EMAIL CF_API_KEY &&
    nix run nixpkgs#flarectl -- dns list --zone ohmymndy.com)
