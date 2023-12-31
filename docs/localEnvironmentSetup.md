# Local Development Setup

To set up your local development environment, follow these steps:


## Pre-requisites

Ensure you have the following installed on your system:

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Docker Compose](https://formulae.brew.sh/formula/docker-compose)

Next, create a new file named `.env` in the root directory and paste the following code:

```sh
# Project Name
PROJECT_NAME=blog-bubbles-api

# Cors Configuration
BACKEND_CORS_ORIGINS=["*"]

#Database Configuration for Compose
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_SERVER=localhost
POSTGRES_DB=app

# JWT Configuration
SECERET_KEY="baevaefbwfbawfbwwf"
ALGORITHM="HS256"

```

## API Server

After installing the prerequisites, run the following commands from the root directory:

```sh
docker-compose up
```

This will start the API server at [http://localhost:8000](http://localhost:8000).

## Rebuilding the API Server

If you make changes to the API server code, you will need to rebuild the Docker image. To do this, run the following command:

```sh
docker-compose up -d --build
```