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
RUN --mount=type=secret,id=.env,mode=0444,required=true \
 cp /run/secrets/.env .env
RUN cat .env
# As an example here we're running the web service with one worker on uvicorn.
CMD exec uvicorn context_handler.app:app --host 0.0.0.0 --port ${PORT} --workers 1
