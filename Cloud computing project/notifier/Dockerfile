FROM python:3.11-slim-bookworm

COPY notifier/requirements.txt ./
RUN pip install -r requirements.txt

WORKDIR /app

ENV PYTHONPATH=/app

COPY notifier/src ./src
COPY proto ./proto

ENTRYPOINT ["python", "src/server.py" ]
