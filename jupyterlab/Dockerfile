FROM elyra/elyra:2.0.1

USER root

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && apt-get update \
    && apt-get install unixodbc-dev libpq-dev graphviz graphviz-dev xdg-utils gcc -y

USER 1000

RUN pip install -U jupyterlab \
    xgboost \
    mlflow \
    imbalanced-learn \
    textblob \
    pyodbc \
    tensorflow \
    xeus-python notebook \
    jupyterlab_execute_time \
    diagrams \
    pygraphviz \
    pefile \
    networkx

RUN jupyter labextension install --no-build \
    @krassowski/jupyterlab_go_to_definition 

RUN mkdir -p /home/jovyan/.jupyter/lab/user-settings/@jupyterlab/notebook-extension \
    && echo '{"recordTiming": true}' > /home/jovyan/.jupyter/lab/user-settings/@jupyterlab/notebook-extension/tracker.jupyterlab-settings

RUN mkdir -p /home/jovyan/.jupyter/lab/user-settings/@krassowski/jupyterlab-lsp \
    && echo '{"continuousHinting": true}' > /home/jovyan/.jupyter/lab/user-settings/@krassowski/jupyterlab-lsp/completion.jupyterlab-settings \
    && echo '{"ignoreMessagesPatterns": ["W293", "W391", "E302"]}' > /home/jovyan/.jupyter/lab/user-settings/@krassowski/jupyterlab-lsp/diagnostics.jupyterlab-settings

RUN jupyter lab build
