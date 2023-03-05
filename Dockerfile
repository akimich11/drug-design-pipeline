FROM apache/airflow:2.5.1

USER root

RUN apt-get update -y
RUN apt-get install libsasl2-dev python-dev libldap2-dev libssl-dev libsnmp-dev -y

COPY requirements.txt requirements.txt

USER airflow
RUN pip install -r requirements.txt
