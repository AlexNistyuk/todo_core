FROM python:3.11.7-slim-bookworm

RUN mkdir /fastapi_todo_core
WORKDIR /fastapi_todo_core

RUN pip3 install poetry
RUN poetry config virtualenvs.create false

COPY pyproject.toml .
COPY poetry.lock .

RUN poetry install --no-dev

COPY . .
