FROM python:3.13
LABEL authors="alexandr"

COPY pyproject.toml uv.lock app/

WORKDIR app

RUN pip3 install --upgrade pip && pip3 install uv
RUN uv sync --no-dev

COPY ./ ./

ENV PATH="/app/.venv/bin:$PATH"
