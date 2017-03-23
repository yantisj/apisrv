# Docker Instructions for Mac

* Install [Docker for Mac](https://docs.docker.com/engine/installation/mac/)
* Copy and edit the docker/env-file to .env
* [ or copy from test at /opt/dcmap/.env ]

* Initialize Docker Environment Variables: ```source docker/start-env.sh```
* Build the images: ```docker-compose build```

* Initialize API database with user/pass from env-file: 
* ```dcmd dcmctl.py --initdb; dcmd dcmctl.py --adduser testuser``` 
* [ or copy from test /opt/dcmap/lib/dcmap.sql to lib/dcmap.sql ]

## Development Version

* Import the test database: ```dcmd ./test/first_import.sh```
* Start Services: ```docker-compose up```
* [Login to the Development website](https://localhost:8443)

## Test/Dev Version

* For full test environment
* Run:: ```docker-compose -f docker-compose.yml -f docker-compose.test.yml up```
* [Login to the Test/Prod website](https://localhost)
