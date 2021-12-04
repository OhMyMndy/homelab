#!/usr/bin/env ash


apk add --no-cache gettext sed grep


cat /config/ddclient-template.conf | sed -E '/^#|^$/d' | envsubst > /ddclient.conf

chown -R abc:abc /config
chmod 775 /config
chmod 775 /config/custom-services.d/
chmod 775 /config/custom-cont-init.d/

mkdir -p /var/cache/ddclient
chown -R abc:abc /var/cache/ddclient