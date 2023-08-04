FROM python:3.10-slim

ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

ENV CODE_ENV DEV
ENV PORT 8080
ENV SENTENCE_TRANSFORMERS_HOME ./.cache/

RUN pip install --no-cache-dir -r requirements.txt

# As an example here we're running the web service with one worker on uvicorn.
CMD exec gunicorn gridoai_ml.app:app -b 0.0.0.0:${PORT} --workers 1 --timeout 300 --log-level=debug --preload --worker-class=uvicorn.workers.UvicornWorker
