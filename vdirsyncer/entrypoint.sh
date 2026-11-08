#!/bin/ash
# Container entrypoint: run `vdirsyncer sync` on a fixed interval.
# Interval is configurable via SYNC_INTERVAL (seconds). Default: 600 (10 min).
set -u

INTERVAL="${SYNC_INTERVAL:-600}"

# Forward SIGTERM/SIGINT so the container stops promptly instead of waiting
# for the current `sleep` to finish.
sleep_pid=""
shutdown() {
  echo "[$(date -u +%FT%TZ)] received signal, shutting down."
  [ -n "$sleep_pid" ] && kill -TERM "$sleep_pid" 2>/dev/null || true
  exit 0
}
trap shutdown TERM INT

echo "[$(date -u +%FT%TZ)] starting vdirsyncer loop (interval=${INTERVAL}s)"

while true; do
  echo "[$(date -u +%FT%TZ)] vdirsyncer sync"
  if ! vdirsyncer sync; then
    echo "[$(date -u +%FT%TZ)] sync failed; will retry in ${INTERVAL}s"
  fi

  # Background sleep + wait so traps fire immediately on signal.
  sleep "$INTERVAL" &
  sleep_pid=$!
  wait "$sleep_pid"
  sleep_pid=""
done
