FROM python:3.12
LABEL authors="alexandr"

WORKDIR app

COPY pyproject.toml uv.lock ./

RUN pip3 install --upgrade pip && pip3 install uv
RUN uv sync --no-dev

COPY app/ ./

ENV PATH="/app/.venv/bin:$PATH"
