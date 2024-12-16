#!/usr/bin/env ash

while true; do
  aria2c -c -d /storage -i /zim-list.txt --show-console-readout false --summary-interval 0 # --on-download-complete /complete.sh

  sleep 86400
done
