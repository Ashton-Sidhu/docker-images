#!/bin/bash

kubectl apply -f airflow-env-configmap.yaml
kubectl apply -f gitsync-env-configmap.yaml
kubectl apply -f airflow.yaml
