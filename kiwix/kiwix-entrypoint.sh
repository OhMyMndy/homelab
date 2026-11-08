#!/usr/bin/env ash
# entrypoint.sh for kiwix container
LIBRARY_DIR="/library"

while true; do
  # snapshot current .zim files
  current=$(ls "$LIBRARY_DIR"/*.zim 2>/dev/null | md5sum)

  kiwix-serve --port 8080 "$LIBRARY_DIR"/*.zim &
  pid=$!

  # poll for changes
  while true; do
    sleep 60
    new=$(ls "$LIBRARY_DIR"/*.zim 2>/dev/null | md5sum)
    if [ "$current" != "$new" ]; then
      kill "$pid"
      wait "$pid" 2>/dev/null
      break
    fi
  done
done
