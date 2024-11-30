FROM python:3.10-alpine

ENV PYTHONBUFFERED=1

COPY . /app/
WORKDIR /app/peak
EXPOSE 8000

ARG DEV=false
RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    /venv/bin/pip install -r /app/requirements.txt && \
    if [$DEV = "true"]; \
        then  /venv/bin/pip install -r /app/requirements.dev.txt ; \
    fi && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

USER django-user
ENV PATH="/venv/bin:$PATH"

CMD ["python", "manage.py", "runserver", "0.0.0.0.:8000"]
