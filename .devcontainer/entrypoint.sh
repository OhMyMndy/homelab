#!/usr/bin/env bash


sudo setcap cap_net_bind_service=ep $(which rootlesskit)

mkdir -p "$XDG_RUNTIME_DIR"
kill -9 "$XDG_RUNTIME_DIR/docker.pid" || true
pkill -e -f -9 containerd
pkill -e -f -9 dockerd
pkill -e -f -9 rootlesskit

rm -rf "$XDG_RUNTIME_DIR/docker*"
rm -rf "/tmp/rootlesskit*"

# DOCKERD_ROOTLESS_ROOTLESSKIT_SLIRP4NETNS_SANDBOX=false
# DOCKERD_ROOTLESS_ROOTLESSKIT_FLAGS="--publish 0.0.0.0:80:80/tcp --publish 0.0.0.0:443:443/tcp"
nohup dockerd-rootless.sh &
