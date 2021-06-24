FROM jupyter/tensorflow-notebook:latest

USER root

RUN apt-get update \
    && apt-get install unixodbc-dev libpq-dev graphviz graphviz-dev xdg-utils gcc g++ -y

USER 1000

COPY packages.txt .

RUN pip install -r packages.txt

RUN ipython profile create \  
    && ipython --IPCompleter.use_jedi=False

COPY start.py /home/jovyan/.ipython/profile_default/startup/start.py

RUN jupyter labextension install --no-build \
    @krassowski/jupyterlab_go_to_definition 

RUN mkdir -p /home/jovyan/.jupyter/lab/user-settings/@krassowski/jupyterlab-lsp \
    && echo '{"continuousHinting": true}' > /home/jovyan/.jupyter/lab/user-settings/@krassowski/jupyterlab-lsp/completion.jupyterlab-settings \
    && echo '{"ignoreMessagesPatterns": ["W293", "W391", "E302"]}' > /home/jovyan/.jupyter/lab/user-settings/@krassowski/jupyterlab-lsp/diagnostics.jupyterlab-settings

RUN jupyter lab build
