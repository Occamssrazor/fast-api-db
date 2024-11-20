FROM python:3.10

RUN apt-get -y update && apt-get install -y postgresql-client
WORKDIR /docker_fast
COPY ./requirements.txt /docker_fast/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /docker_fast/requirements.txt

COPY ./api.py /docker_fast/api.py

EXPOSE 8000
CMD ["uvicorn", "api:app", "--host" "0.0.0.0", "--port", "8000"]
