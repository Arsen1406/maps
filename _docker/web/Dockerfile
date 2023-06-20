FROM python:3.10-slim

RUN mkdir /app
COPY /maps /app/
COPY /requirements.txt /app/
RUN pip install -r /app/requirements.txt --no-cache-dir
WORKDIR /app
COPY . /app
RUN python manage.py runserver
