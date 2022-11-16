FROM python:3.11.0-alpine3.16

ENV NUMBER_OF_USERS 3
ENV TEAMS_INCOMING_WEBHOOK "https://<incoming_webhookt"
ENV MSSQL_CONNECTION_STRING "<connection_string>"

RUN apk add curl gpg gpg-agent unixodbc-dev gcc libc-dev g++ libffi-dev libxml2
RUN pip install poetry

WORKDIR /tmp
RUN curl -O https://download.microsoft.com/download/8/6/8/868e5fc4-7bfe-494d-8f9d-115cbcdb52ae/msodbcsql18_18.1.2.1-1_amd64.apk; \
    curl -O https://download.microsoft.com/download/8/6/8/868e5fc4-7bfe-494d-8f9d-115cbcdb52ae/mssql-tools18_18.1.1.1-1_amd64.apk; \
    apk add --allow-untrusted msodbcsql18_18.1.2.1-1_amd64.apk; \
    apk add --allow-untrusted mssql-tools18_18.1.1.1-1_amd64.apk

COPY ./interviewer/ /root/local/interviewer/interviewer
COPY ./pyproject.toml /root/local/interviewer/pyproject.toml
COPY ./poetry.lock /root/local/interviewer/poetry.lock
COPY ./README.md /root/local/interviewer/README.md
COPY ./main.py /root/local/interviewer/main.py

WORKDIR /root/local/interviewer/

RUN poetry install

CMD ["poetry", "run", "python", "main.py"]
