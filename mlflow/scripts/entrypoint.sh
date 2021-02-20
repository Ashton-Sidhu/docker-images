#!/usr/bin/env bash

# User-provided configuration must always be respected.
#
# Therefore, this script must only derives MlFlow MLFLOW__ variables from other variables
# when the user did not provide their own configuration.

# Global defaults and back-compat
POSTGRES_HOST="${POSTGRES_HOST:-postgres}"
POSTGRES_PORT=5432
POSTGRES_USER="${POSTGRES_USER:-mlflow}"
POSTGRES_PASS="${POSTGRES_PASSWORD:-mlflow}"
POSTGRES_DB="${POSTGRES_DB:-mlflow}"

CONN_STRING="postgresql+psycopg2://${POSTGRES_USER}:${POSTGRES_PASS}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}${POSTGRES_EXTRAS}"

mlflow server \
    --backend-store-uri "${CONN_STRING}" \
    --default-artifact-root "${DEFAULT_ARTIFACT_ROOT}" \
    --host 0.0.0.0
