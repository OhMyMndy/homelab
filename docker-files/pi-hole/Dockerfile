FROM diginc/pi-hole:debian_v3.1

RUN apt-get update \
  && apt-get install vim -y

RUN echo "addn-hosts=/etc/pihole/lan.list" | sudo tee /etc/dnsmasq.d/02-lan.conf