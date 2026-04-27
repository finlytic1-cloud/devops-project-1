# Containerized Flask API with CI/CD

[![CI/CD Pipeline](https://github.com/finlytic1-cloud/devops-project-1/actions/workflows/ci.yml/badge.svg)](https://github.com/finlytic1-cloud/devops-project-1/actions/workflows/ci.yml)

A production-ready Python REST API, containerized with Docker and deployed via an automated CI/CD pipeline using GitHub Actions.

## Architecture

```
Developer push → GitHub Actions → Run tests → Build Docker image → Publish to GHCR
                                       ↓
                                  Fail = block deploy
                                       ↓
                                  Pass = image live
```

## Features

- REST API with health check endpoint
- Production-grade Gunicorn WSGI server
- Automated test suite (pytest)
- CI/CD pipeline with GitHub Actions
- Docker image automatically built and published to GitHub Container Registry on every push to main
- Images tagged with `latest` and commit SHA for easy rollback

## Quick Start

**Pull and run the published image:**
```bash
docker run -p 5000:5000 ghcr.io/finlytic1-cloud/devops-project-1:latest
```

**Or build from source:**
```bash
git clone https://github.com/finlytic1-cloud/devops-project-1
cd devops-project-1
docker compose up -d
```

App available at http://localhost:5000

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/`      | GET    | Returns app info and container hostname |
| `/health`| GET    | Health check for load balancers / Kubernetes probes |

## CI/CD Pipeline

Every push to `main` triggers:

1. **Test job** — Spins up a clean Ubuntu VM, installs dependencies, runs pytest
2. **Build & Publish job** — If tests pass, builds the Docker image and pushes to GitHub Container Registry with two tags:
   - `:latest` for the most recent build
   - `:<commit-sha>` for precise version targeting and rollbacks

Pull requests trigger only the test job, blocking merges if tests fail.

## Tech Stack

- **Language:** Python 3.11
- **Framework:** Flask 3.0
- **Server:** Gunicorn 21.2
- **Containerization:** Docker, Docker Compose
- **CI/CD:** GitHub Actions
- **Registry:** GitHub Container Registry (GHCR)
- **Testing:** pytest

## Project Structure

```
.
├── .github/workflows/
│   └── ci.yml              # GitHub Actions pipeline
├── app/
│   ├── main.py             # Flask application
│   ├── requirements.txt    # Python dependencies
│   └── test_main.py        # Test suite
├── Dockerfile              # Container image definition
├── docker-compose.yml      # Local multi-container orchestration
└── README.md
```
