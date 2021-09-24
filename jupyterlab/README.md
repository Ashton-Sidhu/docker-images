# JupyterLab Docker Image

A fully managed docker container with Jupyter Lab and up to date packages for data science and machine learning. This image is also compatible to be used as a single user instance with Jupyter Hub.

## Features

- Built in debugger
- Linting
- Autocomplete
- Command runtime

## Packages

The latest versions of:
- xgboost
- mlflow
- imbalanced-learn 
- textblob 
- pyodbc 
- xeus-python 
- notebook
- diagrams 
- pygraphviz 
- pefile 
- networkx 
- boto3
- lxml
- ipython-autotime
- jupyterlab-lsp
- python-lsp-server[all]
- shap
- bokeh
- plotly
- altair
- lightgbm
- interpret
- yellowbrick
- statsmodels
- transformers
- elasticsearch-dsl>=7.0.0,<8.0.0
- eland
## Usage

To run this as a standalone Docker container run the following command:

`docker run --rm -p 10000:8888 -v "${PWD}":/home/jovyan/work -e JUPYTER_ENABLE_LAB=yes bigsidhu/jupyter-notebook`

For more configuration options check out the [Jupyter Docker documentation](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/common.html).

## Adding Libraries

See a library you want and it's not there?

Add it to `packages.txt` and submit a PR to this project!
