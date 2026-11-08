#!/usr/bin/env ash

# aria2 passes: GID, number of files, file path
filepath="$3"

cd "$(dirname "$filepath")"

if [[ -f "$filepath" ]]; then
  mv "$filepath" ../
fi
