# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.236.0/containers/ubuntu/.devcontainer/base.Dockerfile

# [Choice] Ubuntu version (use ubuntu-22.04 or ubuntu-18.04 on local arm64/Apple Silicon): ubuntu-22.04, ubuntu-20.04, ubuntu-18.04
ARG VARIANT="jammy"
FROM mcr.microsoft.com/vscode/devcontainers/base:0-${VARIANT}

# uidmap is for docker rootless
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends git uidmap fuse-overlayfs


RUN curl -SsL https://get.docker.com | bash -

USER vscode
ENV XDG_RUNTIME_DIR=/tmp/runtime-dir
RUN mkdir -p "$XDG_RUNTIME_DIR"

# Setup docker
ENV DOCKER_HOST=unix:///$XDG_RUNTIME_DIR/docker.sock