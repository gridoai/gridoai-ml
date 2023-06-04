FROM python:3.10-slim
RUN --mount=type=secret,id=.env,mode=0444,required=true \
 cp /run/secrets/.env .env
RUN cat .env
COPY .env .env

ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

ENV CODE_ENV DEV
ENV PORT 7860
RUN pip install poetry
RUN poetry export --without-hashes --format=requirements.txt > requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the start script
COPY start.sh start.sh

# Use the start script as the command
CMD ["./start.sh"]
