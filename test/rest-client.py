#!/usr/bin/env python3
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
REST API Sample Client
"""
import requests
import json

user = 'testuser'
passwd = 'testpass'
url = 'http://localhost:5000'

# Make a request (don't verify cert if SSL)
r = requests.get(url + '/test/api/v1.0/info?var=testvar', auth=(user, passwd), verify=False)

# Check for proper response
if r.status_code == 200:

    # JSON Dict
    response = r.json()

    # Dump JSON in pretty format
    print(json.dumps(response, sort_keys=True, indent=4, separators=(',', ': ')))
else:
    print("Request Error:", r.status_code, r.text)
