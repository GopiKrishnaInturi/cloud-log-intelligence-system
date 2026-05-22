# Cloud Infrastructure Log Intelligence System

Cloud-native infrastructure monitoring and log intelligence platform built using Python, FastAPI, PostgreSQL, Docker, Redis, and AWS deployment architecture.

## Features

- Infrastructure log ingestion
- Distributed log processing
- Authentication anomaly detection
- Timeout and crash analysis
- Real-time operational monitoring
- Fault analytics
- SQL reporting dashboards
- Containerized deployment

## Run

```bash
docker-compose up --build
```

## Endpoints

- POST /logs
- GET /metrics/errors
- GET /metrics/auth
- GET /health