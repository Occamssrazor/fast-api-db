FROM python:3.10

RUN apt-get -y update && apt-get install -y postgresql-client
WORKDIR /docker_fast
COPY ./requirements.txt /docker_fast/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /docker_fast/requirements.txt

COPY . /docker_fast
