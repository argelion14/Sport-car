FROM python:3.10.1-slim

LABEL maintainer="argelion14"

RUN apt-get update; pip install poetry ;groupadd -r tester && useradd -m -g tester tester

USER tester
WORKDIR /app/test

COPY poetry.lock pyproject.toml tasks.py /app/test/

ENV PATH = "$PATH:/home/tester/.local/bin"

RUN poetry config virtualenvs.create false; poetry install

ENTRYPOINT [ "invoke", "test"]
