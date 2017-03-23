FROM nginx:1.11.7-alpine
MAINTAINER Jonathan Yantis <yantisj@gmail.com>
ENV TZ America/New_York
RUN echo EST5EDT > /etc/TZ
RUN apk add --update openssh tzdata
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf
COPY apisrv-nginx /etc/nginx/conf.d/apisrv-nginx.conf
COPY apisrv-internal-nginx /etc/nginx/conf.d/apisrv-internal-nginx.conf

COPY apisrv.crt /
COPY apisrv.key /
