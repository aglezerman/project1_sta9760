FROM python:3.7

WORKDIR /APP

COPY requirements.txt /APP

RUN pip install -r requirements.txt