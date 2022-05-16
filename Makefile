up:
	docker compose up -d external-service

call-hello-mapping:
	docker compose run --rm curl -i http://external-service/some/thing

define HELLO_MAPPING
{ 
	"request": { 
		"method": "GET",
		"url": "/some/thing"
	},
	"response": {
		"body": "Hello world!",
		"headers": {
			"Content-Type": "text/plain"
		},
		"status": 200
	}
}
endef

export HELLO_MAPPING
add-hello-mapping:
	docker compose run --rm curl -i http://external-service/__admin/mappings -X POST --data-binary "$$HELLO_MAPPING"

reset-mappings:
	docker compose run --rm curl -i http://external-service/__admin/mappings/reset -X POST 

call-my-account-unauthorized:
	docker compose run --rm curl -i http://external-service/my-account -H "Autorization: Bearer invalid.token"

call-my-account-valid-auth:
	docker compose run --rm curl -i http://external-service/my-account -H "Authorization: Bearer a.valid.token"

