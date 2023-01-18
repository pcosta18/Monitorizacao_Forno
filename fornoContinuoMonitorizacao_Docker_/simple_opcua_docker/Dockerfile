FROM python:3.9.16

RUN pip install opcua
RUN pip install psycopg2

COPY . /app

WORKDIR /app

# the -u is for the logs. Otherwise they will buffer.
CMD ["python","-u", "opcua_client.py"]
