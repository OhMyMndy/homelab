#!/usr/bin/env bash

sudo mkdir -p /etc/docker
cat <<EOF | sudo tee /etc/docker/daemon.json
{
  "default-address-pools" : [
    {
      "base" : "172.17.0.0/12",
      "size" : 20
    },
    {
      "base" : "192.168.0.0/16",
      "size" : 24
    }
  ],
  "log-opts": {
    "max-file": "3",
    "max-size": "10m"
  }
}
EOF
