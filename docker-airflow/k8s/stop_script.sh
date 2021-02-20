#!/bin/bash

kubectl delete -f airflow-env-configmap.yaml
kubectl delete -f gitsync-env-configmap.yaml
kubectl delete deployment airflow-scheduler web
