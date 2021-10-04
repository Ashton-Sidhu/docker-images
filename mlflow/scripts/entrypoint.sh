#!/usr/bin/env bash

# User-provided configuration must always be respected.
#
# Therefore, this script must only derives MlFlow MLFLOW__ variables from other variables
# when the user did not provide their own configuration.

# Global defaults and back-compat
POSTGRES_HOST="${POSTGRES_HOST:-postgres}"
POSTGRES_PORT="${POSTGRES_PORT:-5432}"
POSTGRES_USER="${POSTGRES_USER:-postgres}"
POSTGRES_PASSWORD="${POSTGRES_PASSWORD:-postgres}"
POSTGRES_DB="${POSTGRES_DB:-postgres}"
HOST="${HOST:-0.0.0.0}"
PORT="${PORT:-5000}"

CONN_STRING="postgresql+psycopg2://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}${POSTGRES_EXTRAS}"

mlflow server \
    --backend-store-uri "${CONN_STRING}" \
    --default-artifact-root "${DEFAULT_ARTIFACT_ROOT}" \
    --host "${HOST}" \
    --port "${PORT}"
