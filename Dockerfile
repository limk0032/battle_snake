# syntax=docker/dockerfile:1
FROM jupyter/base-notebook:latest
RUN pip install jupyterlab_code_formatter
RUN pip install black isort

