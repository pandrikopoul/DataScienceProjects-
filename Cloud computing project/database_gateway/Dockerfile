FROM python:3.11-slim-bookworm

COPY database_gateway/requirements.txt ./
RUN pip install -r requirements.txt

WORKDIR /app

ENV PYTHONPATH=/app

COPY database_gateway/src ./src
COPY proto ./proto

ENTRYPOINT ["python", "src/server.py" ]
