#!/usr/bin/env bash
set -e
DIR="$(dirname "$(readlink -f "$0")")/../"

cd "$DIR" || exit

source deploy/functions.sh

(source .env-cloudflare && export CF_API_EMAIL CF_API_KEY &&
    nix run nixpkgs#flarectl -- dns create-or-update --zone ohmymndy.com --name '*.home-tailscale' --content $TAILSCALE_IP --type A) || true

(source .env-cloudflare && export CF_API_EMAIL CF_API_KEY &&
    nix run nixpkgs#flarectl -- dns create-or-update --zone ohmymndy.com --name '*.home' --content $LOCAL_IP --type A) || true

start reverse-proxy adguard smtprelay status vaultwarden dashy homepage wallabag \
    redmine tt-rss humblebundle-downloader searxng \
    kiwix pokeblahaj \
    litellm openwebui

(source .env-cloudflare && export CF_API_EMAIL CF_API_KEY &&
    nix run nixpkgs#flarectl -- dns list --zone ohmymndy.com)
