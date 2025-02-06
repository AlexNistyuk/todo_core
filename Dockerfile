FROM python:3.11.7-slim-bookworm as builder

WORKDIR /fastapi_todo_core

RUN pip3 install poetry
RUN poetry config virtualenvs.create false

COPY pyproject.toml .
COPY poetry.lock .

RUN poetry install --no-dev --no-root --no-ansi --no-interaction \
    && poetry export -f requirements.txt -o requirements.txt

FROM python:3.11.7-slim-bookworm as final

WORKDIR /fastapi_todo_core

COPY --from=builder /fastapi_todo_core/requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
