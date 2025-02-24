#!/usr/bin/env bash

set -e

while true; do
  date
  env
  hbd --platform ebook -l /library -s "$HUMBLE_BUNDLE_AUTH_TOKEN" --update --progress --include pdf mobi epub
  # Sleep for 1 day
  sleep 86400
done
