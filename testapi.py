#!/usr/bin/env python3
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
Test the API Application
"""
from base64 import b64encode
import unittest
import tempfile
import apisrv

headers = {
    'Authorization': 'Basic %s' % b64encode(b"testuser:testpass").decode("ascii")
}

class APITestCase(unittest.TestCase):
    """ API Testing Cases"""
    def setUp(self):
        apisrv.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + tempfile.mkstemp()[1]
        apisrv.app.config['TESTING'] = True
        self.app = apisrv.app.test_client()

        with apisrv.app.app_context():
            apisrv.db.create_all()
            try:
                apisrv.user.add_user("testuser", "testpass")
            except Exception:
                pass

    def tearDown(self):
        apisrv.db.drop_all()
    
    def test_index(self):
        rv = self.app.get('/')
        assert b'Authentication required' in rv.data
    
    def test_info(self):
        rv = self.app.get('/test/api/v1.0/info?test=GETTEST', headers=headers)
        assert b'GET test' in rv.data
    
    def test_uptime(self):
        rv = self.app.get('/test/api/v1.0/uptime', headers=headers)
        assert b'load averages' in rv.data

if __name__ == '__main__':
    unittest.main()
