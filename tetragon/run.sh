#!/usr/bin/env bash

set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR" || exit 1

export PODCIDR="127.0.0.1/32"
export SERVICECIDR="127.0.0.1/32"

mkdir -p tetragon.tp.d
rm -f network_egress_cluster.yaml

wget https://raw.githubusercontent.com/cilium/tetragon/main/examples/quickstart/network_egress_cluster.yaml
envsubst <network_egress_cluster.yaml >tetragon.tp.d/network_egress_cluster_subst.yaml

rm network_egress_cluster.yaml

docker compose up -d --force-recreate
