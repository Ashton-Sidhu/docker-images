FROM jupyter/tensorflow-notebook:latest

USER root

RUN apt-get update && apt-get install unixodbc-dev libpq-dev -y

USER 1000

RUN yes | bash -c "$(wget -q -O - https://linux.kite.com/dls/linux/current)"; exit 0

RUN pip install -U jupyterlab \
    xgboost \
    mlflow \
    imbalanced-learn \
    textblob \
    pyodbc \
    xeus-python notebook \
    jupyterlab-git \
    jupyterlab_execute_time \
    elyra \
    jupyterlab-kite

RUN jupyter labextension install --no-build \
    @krassowski/jupyterlab_go_to_definition

RUN jupyter lab build

CMD ["/home/jovyan/.local/share/kite/kited"]
