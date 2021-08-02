FROM ubuntu:latest

RUN apt-get update -y && apt-get install python3-pip -y

RUN apt-get install sqlite3 -y

COPY . /C2-server

WORKDIR C2-server

RUN pip3 install -r requirements.txt

CMD python3 c2-server.py