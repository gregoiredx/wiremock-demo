.PHONY: up
up:
	docker compose up --build -d external-service my-service

.PHONY: integration-tests
integration-tests:
	docker-compose build integration-tests
	docker-compose run --rm integration-tests
