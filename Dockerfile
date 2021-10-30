# syntax=docker/dockerfile:1
FROM jupyter/base-notebook:latest
RUN pip install numpy
RUN pip install matplotlib
RUN pip install jupyterlab_code_formatter
RUN pip install black isort

# sudo docker build -t jupyter_with_formatter:v1 .
# sudo docker run --rm -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -v /home/user1/PycharmProjects/battle_snake:/home/jovyan/work jupyter_with_formatter:v1

