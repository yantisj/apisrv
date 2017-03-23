FROM python:3.6
MAINTAINER Jonathan Yantis <yantisj@musc.edu>
COPY docker/timezone /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata
RUN apt-get update && apt-get install -y \
   build-essential \
   lsb-release

# RUN wget http://packages.couchbase.com/releases/couchbase-release/couchbase-release-1.0-2-amd64.deb
# RUN dpkg -i couchbase-release-1.0-2-amd64.deb
# RUN apt-get update && apt-get install -y libcouchbase-dev

RUN useradd -ms /bin/bash -u 50990 apisrv

RUN mkdir -p /opt/apisrv /etc/apisrv /var/log/apisrv
ENV PATH="/opt/apisrv:${PATH}"
WORKDIR /opt/apisrv
COPY requirements.txt ./
RUN pip3 install --upgrade pip \
&&  pip3 install -r requirements.txt
COPY apisrv.ini /etc/apisrv/
COPY apisrv/ ./apisrv/
COPY ./test/ ./test/
COPY ./extra/ ./extra/
COPY ./lib/ ./lib/
COPY *.py ./
RUN chown -R apisrv /opt/apisrv
RUN chgrp -R apisrv /opt/apisrv
EXPOSE 8080
EXPOSE 9001
CMD ["bash"]
