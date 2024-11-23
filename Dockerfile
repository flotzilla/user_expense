FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip install poetry

RUN poetry config virtualenvs.create false \
    && poetry install --no-root

EXPOSE ${APP_PORT}

ENTRYPOINT ["./expenses/scripts/run.sh"]
