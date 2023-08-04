include .env

PROJECT_ID:=lucid-arch-387422
APP_NAME:=gridoai_ml
APP_NAME_WITH_HYPHEN:=gridoai-ml
MEMORY:=6000Mi
CPU:=2

run:
	@poetry run uvicorn $(APP_NAME).app:app --reload

test:
	@poetry run pytest

build:
	poetry export --without-hashes --format=requirements.txt > requirements.txt
	docker build -t dev_$(APP_NAME) .

gcloud-build:
	poetry export --without-hashes --format=requirements.txt > requirements.txt
	gcloud builds submit --region=us-west2 \
	--tag us-west2-docker.pkg.dev/$(PROJECT_ID)/docker-repo/$(APP_NAME) \
	--verbosity=debug

gcloud-run:
	gcloud run deploy dev-$(APP_NAME_WITH_HYPHEN)-br \
	--image us-west2-docker.pkg.dev/$(PROJECT_ID)/docker-repo/$(APP_NAME) \
	--cpu $(CPU) \
	--memory $(MEMORY) \
	--platform managed \
	--region southamerica-east1 \
	--allow-unauthenticated
