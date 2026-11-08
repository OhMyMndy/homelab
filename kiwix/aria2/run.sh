#!/usr/bin/env ash

mkdir -p /library/incomplete

cd /library/incomplete
while true; do
	# rebuild input file, skipping already-downloaded .zim files
	while IFS= read -r url; do
		filename=$(basename "$url")
		if [ ! -f "/library/$filename" ]; then
			echo "$url"
			echo "  out=${filename}"
		fi
	done </zim-list.txt >/tmp/zim-list.txt

	cat /tmp/zim-list.txt

	# only run aria2 if there's something to download
	if [ -s /tmp/zim-list.txt ]; then
		aria2c -c -d /library/incomplete -i /tmp/zim-list.txt \
			--show-console-readout false \
			--summary-interval 0 \
			--enable-rpc \
			--max-connection-per-server=1 \
			--on-download-complete /complete.sh
	fi

	sleep 86400
done
