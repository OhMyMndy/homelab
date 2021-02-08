FROM ubuntu:20.04
#FROM ydkn/cups:latest

RUN apt update; DEBIAN_FRONTEND=noninteractive apt install curl usbutils cups -y -qq

RUN curl -SsL https://whp-hou4.cold.extweb.hp.com/pub/softlib/software13/printers/SS/SL-C4010ND/uld_V1.00.39_01.17.tar.gz | tar xz \
        && yes | ./uld/install.sh \
        && rm -rf uld
# RUN mkdir -p /var/log/cups && ln -sf /dev/stderr /var/log/cups/error_log
CMD cupsd -f -c /etc/cups/cupsd.conf
