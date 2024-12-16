#!/usr/bin/env bash

set -e

while true; do
  date
  env
  hbd  --platform ebook -l /library -s "$HUMBLE_BUNDLE_AUTH_TOKEN" --update --progress;
  # Sleep for 7 days
  sleep 604800
done

