CONSUMER_IMG = consumer-img
DATABASE_GATEWAY_IMG = database-gateway-img
NOTIFIER_IMG = notifier-img
REST_API_IMG = rest-api-img

CONSUMER_CONTAINER = consumer
DATABASE_GATEWAY_CONTAINER = database-gateway
NOTIFIER_CONTAINER = notifier
REST_API_CONTAINER = rest-api

NETWORK = cloud-computing

build_consumer:
	docker build -f consumer/Dockerfile -t $(CONSUMER_IMG) .

build_database_gateway:
	docker build -f database_gateway/Dockerfile -t $(DATABASE_GATEWAY_IMG) .

build_notifier:
	docker build -f notifier/Dockerfile -t $(NOTIFIER_IMG) .

build_rest_api:
	docker build -f rest_api/Dockerfile -t $(REST_API_IMG) .


run_consumer:
	docker run --rm --network $(NETWORK)  --name $(CONSUMER_CONTAINER) $(CONSUMER_IMG)

run_database_gateway:
	docker run --rm --network $(NETWORK) --name $(DATABASE_GATEWAY_CONTAINER) $(DATABASE_GATEWAY_IMG)

run_notifier:
	docker run --rm --network $(NETWORK) --name $(NOTIFIER_CONTAINER) $(NOTIFIER_IMG)

run_rest_api:
	docker run --rm --network $(NETWORK) --name $(REST_API_CONTAINER) -p 3003:3003 $(REST_API_IMG)

run_mongo_db:
	docker run --rm --network $(NETWORK) --name mongo -d mongo:4.4.6

# Build all services
all: build_consumer build_database_gateway build_notifier build_rest_api

.PHONY: all

