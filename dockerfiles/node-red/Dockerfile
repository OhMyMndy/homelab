FROM nodered/node-red:1.2.5
LABEL maintainer "Mandy Schoep <mandyschoep@gmail.com>"

USER root

RUN apk add --no-cache bash
SHELL [ "/bin/bash", "-o", "pipefail", "-c" ]


ENV PUID="1000"
ENV PGID="1000"
ENV USER="node-red"
ENV HOME="/data"

ARG OVERLAY_VERSION="v1.22.1.0"
ARG OVERLAY_ARCH="amd64"
ADD https://github.com/just-containers/s6-overlay/releases/download/${OVERLAY_VERSION}/s6-overlay-${OVERLAY_ARCH}.tar.gz /tmp/
RUN apk add --no-cache tar
RUN tar xzf /tmp/s6-overlay-${OVERLAY_ARCH}.tar.gz -C /


RUN mkdir -p /etc/cont-init.d
ADD https://raw.githubusercontent.com/OhMyMndy/dockerfiles/master/dockerfiles/shared/root/etc/cont-init.d/20-adduser /etc/cont-init.d/20-adduser
RUN printf "#!/usr/bin/with-contenv bash\nmkdir -p /data && chown -R \$PGID:\$PGID /data" > /etc/cont-init.d/90-chown-data
RUN cat /etc/cont-init.d/90-chown-data


RUN chmod -R +x /etc/cont-init.d/

RUN npm install node-red-contrib-spotify \
    && npm install node-red-dashboard \
    && npm install node-red-contrib-cast \
    && npm install node-red-contrib-castv2 \
    && npm install node-red-node-youtube \
    && npm install node-red-contrib-cron-plus \
    # && npm install node-red-node-serialport \
    # && npm install node-red-contrib-zigbee2mqtt \
    && npm install node-red-contrib-home-assistant-websocket \
    && npm install node-red-contrib-influxdb \
    # && npm install node-red-contrib-oled \
    && npm install node-red-contrib-sqlstring \
    && npm install node-red-contrib-alexa-smart-home \
    && npm install node-red-contrib-zip \
    && npm install node-red-node-sqlite \
    && npm install node-red-contrib-cpu \
    && npm install node-red-contrib-discord \
    && npm install node-red-contrib-wled \
    && npm install node-red-contrib-dockerode \
    && npm install node-red-contrib-heater-controller \
    && npm install node-red-contrib-fritzapi \
    && npm install node-red-contrib-home-assistant-llat \
    && npm install node-red-contrib-mpd \
    && npm install node-red-contrib-light \
    && npm install node-red-contrib-alarm \
    && npm install node-red-contrib-buienradar \
    && npm install node-red-contrib-node-hue \
    && npm install node-red-contrib-avr-yamaha

RUN npm install node-red-contrib-tradfri \
    && npm install node-red-contrib-life

#RUN npm install node-red-contrib-python-function \
RUN npm install node-red-contrib-tv-bravia \
    && npm install node-red-node-wol

RUN apk add --no-cache libcoap


ENTRYPOINT [ "/init" ]
CMD s6-setuidgid $USER npm start --cache /data/.npm -- --userDir /data
