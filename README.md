## Overview

Python Flask-based API server template for creating a secure REST API. This
server has everything you need properly configured out of the box to create your
own API. You can use it to call local scripts, relay to other APIs, or do
anything you can do in Python. Clients can be anything that supports REST calls
(curl, bash, powershell etc). Currently apisrv only supports local authentation,
but it could be extended with LDAP support and auth tokens. Please contact me at
([yantisj](https://github.com/yantisj)) for any help.

## Requirements
* Python 3.4+
* VirtualEnv
* SSL Certificates (can test with non-HTTPS but should not be used in production)

## Features
* Built-in SSL server
* Example functions for creating your own secure API
* Sample Rest Client
* Strong Password Hashing (stored in sqlite DB)
* Rate limiting for safety
* JSONified error handling
* Extensive logging to both stdout and log files

## Installing
* Make sure you have virtualenv and Python3 installed on your system (pip3 install virtualenv)
* Clone the repo: ```git clone https://git.musc.edu/yantisj/apisrv.git```
* Install the virtualenv: ```cd apisrv; virtualenv venv```
* Activate the virtual environment: ```source venv/bin/activate```
* Install Python Requirements: ```pip3 install -r requirements.txt```

## Testing
* You must activate the virtualenv before starting the server
* Initialize DB and Add a user: ```./ctlsrv.py --init; ./ctlsrv.py --add testuser```
* Use the password testpass for the examples below
* Start the server: ```./runsrv.py```
* Test the info request with a browser: [/test/api/v1.0/info?testvar=testing](http://localhost:5000/test/api/v1.0/info?testvar=testing)
* Test via CURL: ```curl -u testuser:testpass http://localhost:5000/test/api/v1.0/info?var1=test```
* Test via the Sample Rest Client: ```./test/rest-client.py```
* Get the system uptime/load: [/test/api/v1.0/uptime](http://localhost:5000/test/api/v1.0/uptime)

## Customizing For Use
* See [api.conf](api.conf)
* Enable https and add a certificate to enable listening beyond localhost
* Add custom methods to [apisrv/views.py](apisrv/views.py)
* Make sure to add the @auth.login_required decorator to each method for security
* Be careful when making system calls with user input
* Check the API rate limits in [apisrv/\_\_init\_\_.py](apisrv/__init__.py)

## Using VirtualEnv with Visual Studio Code
* Make sure you have the latest version of the Python Extension installed
* Use Command+Shift+P: Python: Select Workspace Interpreter and choose python under venv/bin

## Running in Production with Docker

The docker environment changes the API server port to 9000 and runs it behind nginx. Replace the apisrv.crt and apisrv.key certificate files in the nginx directory with valid certs for production. Everything runs as the apisrv user in the container.

* Copy the docker/env-file to .env and customize
* Source the docker start-env file: ```source docker/start-env.sh```
* Copy the SQL database to lib/: ```mkdir lib; cp api.sql lib/```
* Build the docker images: ```docker-compose build```
* Bring up the API server: ```docker-compose up```
* Optionally attach to the container: ```att_api```


## Further Reading
* [Creating a REST API](https://realpython.com/blog/python/api-integration-in-python/)
