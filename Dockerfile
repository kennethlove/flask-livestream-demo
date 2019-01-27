FROM python:3.7-alpine

ENV PYTHONBUFFERED 1
COPY . /code/
WORKDIR /code/
RUN pip install -r /code/requirements.txt

EXPOSE 5000
