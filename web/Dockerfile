FROM ubuntu:latest
MAINTAINER AAYUSH "aayushkumar08@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /run
WORKDIR /run
RUN pip install -r requirements.txt
RUN pip install uwsgi
ADD . /webapp
ENV HOME /webapp
WORKDIR /webapp
EXPOSE 5000
ENTRYPOINT ["uwsgi"]
