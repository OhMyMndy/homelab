FROM homeassistant/home-assistant:stable


RUN pip3 install pytradfri[async]

RUN apk add --no-cache libcoap


RUN wget -q -O - https://hacs.xyz/install | bash -