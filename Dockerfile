FROM python:3.10.1-slim-bullseye

LABEL maintainer="argelion14@gmail.com"

RUN pip install poetry ;groupadd -r tester && useradd -m -g tester tester

USER tester
WORKDIR /home/tester

COPY poetry.lock pyproject.toml tasks.py ./

RUN poetry config virtualenvs.create false; poetry install

WORKDIR /app/test

ENV PATH = "$PATH:/home/tester/.local/bin"

ENTRYPOINT [ "invoke", "test"]