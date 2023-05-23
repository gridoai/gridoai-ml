include .env

run:
	@USE_MOCKED_MODEL=$(USE_MOCKED_MODEL) poetry run python main.py