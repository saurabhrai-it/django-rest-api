FROM python:3.7-alpine
MAINTAINER Learner Club

ENV PYTHONUNBUFFERED 1 # Run python in Docker in unbuffered mode

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt