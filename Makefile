include .env

PROJECT_ID:=lucid-arch-387422
APP_NAME:=gridoai_ml
APP_NAME_WITH_HYPHEN:=gridoai-ml
MEMORY:=6000Mi
CPU:=2

run:
	@poetry run hypercorn gridoai_ml.app:app -b 127.0.0.1:8000 --workers 1 --log-level=debug --worker-class=asyncio

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

modal-setup:
	poetry run python -m modal setup

modal-deploy:
	poetry run python -m modal deploy gridoai_ml/modal_app.py

modal-serve:
	poetry run python -m modal serve gridoai_ml/modal_app.py
