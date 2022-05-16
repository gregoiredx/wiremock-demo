up:
	docker compose up --build -d external-service my-service
integration-tests:
	docker-compose build integration-tests
	docker-compose run --rm integration-tests
