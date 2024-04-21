#!/usr/bin/env bash


export TAILSCALE_IP

TAILSCALE_IP="$(ip -f inet addr show tailscale0 | sed -En -e 's/.*inet ([0-9.]+).*/\1/p')"
