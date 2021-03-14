FROM ubuntu:bionic
RUN apt-get update && apt-get install -y python3 python3-pip
ADD . /opt/magicurl
RUN cd /opt/magicurl && make install
EXPOSE 2408
CMD ["/usr/bin/python3", "/usr/local/bin/magicurl"]
