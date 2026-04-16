FROM python:3.12

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN mkdir /tests_app
WORKDIR /tests_app

COPY pyproject.toml .

RUN pip install --upgrade pip && pip install uv
RUN uv pip install --group dev --system

COPY ./src/ ./src
COPY ./tests/ ./tests

ENTRYPOINT ["pytest", "tests/"]
