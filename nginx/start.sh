#!/bin/sh

if [ -f /.dockerenv ]
then
    cd /
    case $1 in
        all)
          for file in apisrv-nginx apisrv-internal-nginx httpsrv-nginx http-redirect-nginx 
          do
            [ -f $file ] && mv -v $file /etc/nginx/conf.d/$file.conf 
          done
          echo "starting nginx for api and http"
        ;;
        api)
          for file in apisrv-nginx apisrv-internal-nginx
          do
            [ -f $file ] && mv -v $file /etc/nginx/conf.d/$file.conf 
          done
          rm -vf httpsrv-nginx http-redirect-nginx
          echo "starting nginx for api"
        ;;
        http)
          for file in httpsrv-nginx http-redirect-nginx
          do
            [ -f $file ] && mv -v $file /etc/nginx/conf.d/$file.conf 
          done
          rm -vf apisrv-nginx apisrv-internal-nginx
          echo "starting nginx for http"
        ;;
        *)
          echo "Must specify either api or http in script"
          exit 1
        ;;
    esac
    nginx -g 'daemon off;'
else
  echo "Not in container"
  exit 1
fi