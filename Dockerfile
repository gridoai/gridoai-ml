FROM python:3.10-slim

ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR $APP_HOME

COPY . ./

ENV CODE_ENV DEV
ENV PORT 7860

RUN pip install poetry
RUN poetry export --without-hashes --format=requirements.txt > requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Use the start script as the command
CMD echo $GCP_KEY > /tmp/service-account-file.json && \
    export GOOGLE_APPLICATION_CREDENTIALS=/tmp/service-account-file.json && \
    uvicorn context_handler.app:app --host 0.0.0.0 --port ${PORT} --workers 1
