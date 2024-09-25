FROM python:3.10-alpine

ENV PYTHONBUFFERED=1

COPY . /app/
WORKDIR /app
EXPOSE 8000


RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r /app/requirements.txt && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

USER django-user
ENV PATH="/venv/bin:$PATH"

