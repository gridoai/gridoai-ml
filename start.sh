#!/bin/sh
set -a
. ./.env
set +a
exec uvicorn context_handler.app:app --host 0.0.0.0 --port ${PORT} --workers 1
