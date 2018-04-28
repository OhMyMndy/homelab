up: stop
	docker-compose up -d

restart: stop up
	
stop:
	docker-compose stop

rm:
	docker-compose rm -f

build:
	docker-compose build