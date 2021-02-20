FROM jupyter/tensorflow-notebook:latest

USER root

RUN apt-get update && apt-get install unixodbc-dev libpq-dev -y

USER 1000

RUN pip install -U jupyterlab xgboost mlflow imbalanced-learn textblob pyodbc
