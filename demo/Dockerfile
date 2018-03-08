FROM python:2

WORKDIR /usr/src/cdb
COPY config /usr/src/cdb
RUN mkdir /usr/src/cdb/CDB

VOLUME /usr/src/cdb/CDB
CMD ["python", "createCDB.py"]
