FROM python:3.11.0-buster

ENV NUMBER_OF_USERS 3
ENV TEAMS_INCOMING_WEBHOOK "https://<incoming_webhookt"
ENV MSSQL_CONNECTION_STRING "<connection_string>"

RUN apt-get update
RUN apt-get install -y curl gpg gpg-agent unixodbc-dev gcc libc-dev g++ libffi-dev libxml2 apt-utils apt-transport-https
RUN pip install --upgrade pip
RUN pip install poetry

WORKDIR /tmp
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update

RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17
RUN ACCEPT_EULA=Y apt-get install -y mssql-tools
RUN ACCEPT_EULA=Y apt-get install -y unixodbc-dev

COPY ./interviewer/ /root/local/interviewer/interviewer
COPY ./pyproject.toml /root/local/interviewer/pyproject.toml
COPY ./poetry.lock /root/local/interviewer/poetry.lock
COPY ./README.md /root/local/interviewer/README.md
COPY ./main.py /root/local/interviewer/main.py

WORKDIR /root/local/interviewer/

RUN poetry install

CMD ["poetry", "run", "python", "main.py"]
