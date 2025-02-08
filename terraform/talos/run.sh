#!/usr/bin/env bash
set -e
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR" || exit 1

# vmids=( 366 368 369 370) # VMIDs of VMs to delete
# for vmid in "${vmids[@]}"
# do
#     status=$(qm status "$vmid")
#     if [ "$status" = "status: running" ]; then
#       qm stop $vmid
#     fi
#     qm destroy $vmid
# done

tofu_args=
if [[ -f terraform.tfstate ]]; then
  tofu_args="-parallelism=1"
fi
time tofu apply -auto-approve $tofu_args

# Sleep for a bit to give the Talos machines some time to get ready
if [[ "$tofu_args" == '' ]]; then
  sleep 60
fi

mkdir -p ~/.kube ~/.talos
tofu output -raw kubeconfig >~/.kube/config
tofu output -raw talosconfig >~/.talos/config

# TODO: add specific cilium version
# TODO: update or install somehome
time cilium install \
  --set ipam.mode=kubernetes \
  --set kubeProxyReplacement=true \
  --set securityContext.capabilities.ciliumAgent="{CHOWN,KILL,NET_ADMIN,NET_RAW,IPC_LOCK,SYS_ADMIN,SYS_RESOURCE,DAC_OVERRIDE,FOWNER,SETGID,SETUID}" \
  --set securityContext.capabilities.cleanCiliumState="{NET_ADMIN,SYS_ADMIN,SYS_RESOURCE}" \
  --set cgroup.autoMount.enabled=false \
  --set cgroup.hostRoot=/sys/fs/cgroup \
  --set k8sServiceHost=localhost \
  --set k8sServicePort=7445 \
  --set gatewayAPI.enabled=true \
  --set gatewayAPI.enableAlpn=true \
  --set gatewayAPI.enableAppProtocol=true \
  --wait || true

IP_ADDRESS=10.0.40.69
export IP_ADDRESS

helm repo add rook-release https://charts.rook.io/release
helm upgrade --install --create-namespace --namespace rook-ceph rook-ceph rook-release/rook-ceph
kubectl label namespace rook-ceph pod-security.kubernetes.io/enforce=privileged
helm upgrade --install --create-namespace --namespace rook-ceph rook-ceph-cluster --set operatorNamespace=rook-ceph rook-release/rook-ceph-cluster

kubectl create namespace metallb || true
kubectl label namespace metallb pod-security.kubernetes.io/enforce=privileged

kubectl create namespace prometheus || true
kubectl label namespace prometheus pod-security.kubernetes.io/enforce=privileged

kubectl create namespace ingress-nginx || true
kubectl label namespace ingress-nginx pod-security.kubernetes.io/enforce=privileged

helmfile -f helmfile.yaml sync --color
