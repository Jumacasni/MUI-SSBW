FROM python:3.7-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get update && apt-get install -y gettext libgettextpo-dev && pip install -r requirements.txt
COPY . /code/