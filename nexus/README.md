# Sonatype Nexus

Using the Ubuntu apt proxy:

```bash
cat <<EOF | tee /etc/apt/sources.list.d/ubuntu.sources >/dev/null
Types: deb
URIs: https://nexus.home.ohmymndy.com/repository/apt-ubuntu-24.04/
Suites: noble noble-updates noble-backports
Components: main universe restricted multiverse
Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg

## Ubuntu security updates. Aside from URIs and Suites,
## this should mirror your choices in the previous section.
Types: deb
URIs: https://nexus.home.ohmymndy.com/repository/apt-ubuntu-24.04/
Suites: noble-security
Components: main universe restricted multiverse
Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg
EOF

touch /etc/apt/apt.conf.d/99verify-peer.conf \
&& echo >>/etc/apt/apt.conf.d/99verify-peer.conf "Acquire { https::Verify-Peer false }"
```

Using the Dockerhub proxy:

```
docker pull dockerhub.nexus.home.ohmymndy.com/ubuntu:24.04
```
