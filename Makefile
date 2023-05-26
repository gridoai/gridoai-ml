include .env

run:
	@USE_MOCKED_MODEL=$(USE_MOCKED_MODEL) poetry run uvicorn context_handler.app:app --reload