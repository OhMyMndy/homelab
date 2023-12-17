#!/usr/bin/env bash
set -e

trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT

#k3s kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.13.3/cert-manager.yaml

export KUBECONFIG=/etc/rancher/k3s/k3s.yaml

if ! kubectl get namespace argocd &>/dev/null; then
    kubectl create namespace argocd
fi

kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Wait for argocd to be ready
kubectl rollout status deployment argocd-server -n argocd --watch

kubectl port-forward svc/argocd-server -n argocd 8080:443 &>/dev/null &

if kubectl get secret -n argocd argocd-initial-admin-secret &>/dev/null; then
    argocd login --insecure --username admin --password "$(argocd --insecure --grpc-web admin initial-password -n argocd | head -1)" localhost:8080

    argocd account --account admin update-password --current-password "$(argocd --insecure --grpc-web admin initial-password -n argocd | head -1)" --new-password "12341234" 

    kubectl delete secret -n argocd argocd-initial-admin-secret 
fi


# kubectl patch app APP_NAME -p '{"metadata": {"finalizers": null}}' --type merge
# TODO make revision variable so it can be tested with other branches
argocd app create applications \
    --repo https://github.com/ohmymndy/homelab.git \
    --revision k8s \
    --path argocd --dest-server https://kubernetes.default.svc --dest-namespace default \
    --sync-policy auto
# helm repo add firefly-iii https://firefly-iii.github.io/kubernetes/
# helm repo updatehelm repo add firefly-iii https://firefly-iii.github.io/kubernetes/
# helm repo update