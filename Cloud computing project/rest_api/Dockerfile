FROM python:3.11-slim-bookworm

RUN pip install pipenv

WORKDIR /app

COPY rest_api/Pipfile rest_api/Pipfile.lock ./
RUN pipenv install --system --deploy

COPY rest_api/src ./src
COPY proto ./proto

CMD ["gunicorn", "-w", "4", "src.main:app", "--bind", "0.0.0.0:3003", "--worker-class", "uvicorn.workers.UvicornWorker"]
