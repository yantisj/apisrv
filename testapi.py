#!/usr/bin/env python
# Copyright (c) 2016 "Jonathan Yantis"
#
#    This program is free software: you can redistribute it and/or  modify
#    it under the terms of the GNU Affero General Public License, version 3,
#    as published by the Free Software Foundation.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#    As a special exception, the copyright holders give permission to link the
#    code of portions of this program with the OpenSSL library under certain
#    conditions as described in each individual source file and distribute
#    linked combinations including the program with the OpenSSL library. You
#    must comply with the GNU Affero General Public License in all respects
#    for all of the code used other than as permitted herein. If you modify
#    file(s) with this exception, you may extend this exception to your
#    version of the file(s), but you are not obligated to do so. If you do not
#    wish to do so, delete this exception statement from your version. If you
#    delete this exception statement from all source files in the program,
#    then also delete it in the license file.
#
#
"""
Test the API Application
"""
import os
import apisrv
import unittest
import tempfile
from base64 import b64encode

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
