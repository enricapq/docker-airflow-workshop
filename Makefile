all:
	@echo "make build -- build docker images"
	@echo "make up -- run containers"
	@echo "make down -- stop all containers"
	@echo "make tty -- launch bash from worker container"

build:
	docker build --rm -t enrica/docker-airflow .

up:
	docker-compose -f docker-compose.yml up -d
	@echo airflow running on http://localhost:8080 or http://192.168.99.100:8080

down:
	docker-compose -f docker-compose.yml down

tty:
	$(eval WORKER_ID=$(shell docker-compose -f docker-compose.yml ps -q worker))
	docker exec -it $(WORKER_ID) bash