# VERSION 
# AUTHOR: Ashton Sidhu
# DESCRIPTION: Basic MlFlow Tracking Container
# BUILD: docker build --rm -t bigsidhu/docker-mlflow .
# SOURCE: 

FROM python:3.7-slim-buster
LABEL maintainer="Ashton Sidhu"

# Never prompt the user for choices on installation/configuration of packages
ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux

# MLFlow
ARG MLFLOW_USER_HOME=/home/mlflow

# Define en_US.
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV LC_CTYPE en_US.UTF-8
ENV LC_MESSAGES en_US.UTF-8

RUN useradd -ms /bin/bash -d ${MLFLOW_USER_HOME} mlflow \
    && pip install mlflow \
    && pip install psycopg2-binary \
    && chown -R mlflow: ${MLFLOW_USER_HOME}

EXPOSE 5000

COPY scripts/entrypoint.sh /entrypoint.sh

USER mlflow
WORKDIR ${MLFLOW_USER_HOME}
ENTRYPOINT ["/entrypoint.sh"]
