FROM python:3.11-slim-bookworm

COPY consumer/requirements.txt ./
RUN pip install -r requirements.txt

VOLUME ["/app/auth"]

WORKDIR /app

ENV PYTHONPATH=/app

COPY consumer/src ./src
COPY proto ./proto

ENTRYPOINT ["python", "src/consumer.py" ]
