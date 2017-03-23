#!/bin/bash
# Run with source ./start-env.sh

# Useful Aliases
alias dkc='docker-compose'
alias dcmd='docker-compose run cmd'
alias att_api='docker exec -i -t apisrv_apisrv_1 /bin/bash'

export APISRV_docker_env=.env
export APISRV_docker_libdir=./lib/
export APISRV_docker_logdir=./log/
export APISRV_docker_data_dir=./data/
export APISRV_docker_loghost=udp://127.0.0.1:514

## Ports

# API (always https)
export APISRV_docker_api_port=9000
