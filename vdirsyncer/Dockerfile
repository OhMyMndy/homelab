FROM alpine

RUN adduser mandy -u 1000 -D -s /bin/bash

RUN apk add --no-cache vdirsyncer

USER mandy

RUN mkdir -p ~/.vdirsyncer
VOLUME [ "/home/mandy/.vdirsyncer" ]
COPY ./entrypoint.sh /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]
CMD []
# CMD [ "vdirsyncer", "sync" ]
