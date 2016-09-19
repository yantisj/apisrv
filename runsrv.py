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
Run API Server
"""
import logging
from apisrv import app, debug, config

logger = logging.getLogger('runsrv')

# Production server in HTTPS Mode
if config['apisrv']['https'] != '0':
    context = (config['apisrv']['ssl_crt'], config['apisrv']['ssl_key'])
    app.run(host='0.0.0.0', port=int(config['apisrv']['port']), \
            ssl_context=context, threaded=True, debug=debug)

# Localhost-only HTTP development server
else:
    logger.warning("HTTPS is not configured, defaulting to localhost only")
    app.run(debug=debug, port=int(config['apisrv']['port']))
