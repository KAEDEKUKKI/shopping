# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /workspace
COPY requirements.txt /workspace/
RUN pip install -r requirements.txt
COPY . /workspace/
