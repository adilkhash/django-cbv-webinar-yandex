FROM python:3.7.6-slim-buster

RUN apt-get update \
   && apt-get -y install build-essential \
   libpq-dev libssl-dev libffi-dev \
   libxml2-dev libxslt1-dev libssl1.1 \
   postgresql-client

RUN mkdir /code
COPY . /code
WORKDIR /code
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --no-input

CMD python manage.py migrate && gunicorn django_cbv.wsgi -b 0.0.0.0:9000
