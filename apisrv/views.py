#!/usr/bin/env python
#
# Copyright (c) 2016 Jonathan Yantis
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
"""
API Views for serving user requests with examples
Add your own methods here
"""
import logging
import subprocess
from flask import jsonify, request
from apisrv import app, auth, config

# Setup
logger = logging.getLogger(__name__)
app_name = config['apisrv']['app_name']

# http://localhost:5000/test unauthenticated response of "Hello World"
@app.route('/test')
def app_test():
    """ Test Method, no authentication required """
    logger.info("Hello World Requested")
    response = {"message": "Hello World!", "status": "200"}
    return jsonify(response)

# System Uptime, requires authentication
@app.route('/' + app_name + '/api/v1.0/uptime')
@auth.login_required
def app_uptime():
    """ Runs a system command to get the uptime"""
    p = subprocess.Popen('uptime', stdout=subprocess.PIPE, universal_newlines=True)
    uptime = p.stdout.readlines()[0].strip()
    response = {"message": uptime, "status": "200"}
    return jsonify(response)

# Call echo shell cmd on message via /musc/api/v1.0/echo?message=testing
@app.route('/' + app_name + '/api/v1.0/echo', methods=['GET'])
@auth.login_required
def app_echo():
    """ Runs the echo command with input 'message'
        Note: Input is validated and escaped properly
    """
    message = request.args.get('message', '')
    if message:
        p = subprocess.Popen(['echo', message], stdout=subprocess.PIPE, universal_newlines=True)
        uptime = p.stdout.readlines()[0].strip()
        response = {"message": uptime, "status": "200"}
        return jsonify(response)
    else:
        return jsonify({"error": "Must provide message attribute via GET"})

# Info method, Return Request Data back to client as JSON
@app.route('/' + app_name + '/api/v1.0/info', methods=['POST', 'GET'])
@auth.login_required
def app_getinfo():
    """ Returns Flask API Info """
    response = dict()
    response['message'] = "Flask API Data"
    response['status'] = "200"
    response['method'] = request.method
    response['path'] = request.path
    response['remote_addr'] = request.remote_addr
    response['user_agent'] = request.headers.get('User-Agent')

    # GET attributes
    for key in request.args:
        response['GET ' + key] = request.args.get(key, '')
    # POST Attributes
    for key in request.form.keys():
        response['POST ' + key] = request.form[key]

    return jsonify(response)

@app.route('/')
def app_index():
    """Index identifying the server"""
    response = {"message": app_name + \
                " api server: Authentication required for use",
                "status": "200"}
    return jsonify(response)
