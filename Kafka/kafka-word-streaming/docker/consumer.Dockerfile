FROM python:3.10.6-buster

COPY ./src/consumer.py /consumer.py
COPY ./src/requirements.txt /requirements.txt

RUN pip install -r /requirements.txt