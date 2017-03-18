up: stop
	docker-compose up -d
	./scripts/pihole_set_ip

restart: stop up
	
stop:
	docker-compose stop

rm:
	docker-compose rm -f
