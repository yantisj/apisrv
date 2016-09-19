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
Manage the API Server
"""
import sys
import getpass
import apisrv
import argparse

# Config File
config = apisrv.config

parser = argparse.ArgumentParser()

parser = argparse.ArgumentParser(prog='ctlsrv.py',
                                 description='Manage the API Server')

parser.add_argument("--adduser", metavar="user", help="Add API User to DB", type=str)
parser.add_argument("--newpass", metavar="user", help="Update Password", type=str)
parser.add_argument("--testuser", metavar="user", help="Test Authentication", type=str)
parser.add_argument("--deluser", metavar="user", help="Delete API User", type=str)
parser.add_argument("--initdb", help="Initialize the Database", action="store_true")
parser.add_argument("--debug", help="Set debugging level", type=int)
parser.add_argument("-v", help="Verbose Output", action="store_true")

args = parser.parse_args()

verbose = 0
if args.v:
    verbose = 1
if args.debug:
    verbose = args.debug

# Initialize the Database
if args.initdb:
    apisrv.db.create_all()
    apisrv.db.session.commit()

# Add user to DB
elif args.adduser:

    passwd = getpass.getpass('Password:')
    verify = getpass.getpass('Verify Password:')

    if passwd == verify:
        phash = apisrv.user.add_user(args.adduser, passwd)
        if phash:
            print("Successfully Added User to Database")
        else:
            print("Error: Could not Add User to Database")
    else:
        print("Error: Passwords do not match")
    
# Update User Password
elif args.newpass:
    passwd = getpass.getpass('New Password:')
    verify = getpass.getpass('Verify Password:')

    if passwd == verify:
        phash = apisrv.user.update_password(args.newpass, passwd)
        if phash:
            print("Successfully Updated Password")
        else:
            print("Error: Could not Update Password")
    else:
        print("Error: Passwords do not match")

# Delete a User
elif args.deluser:
    ucheck = apisrv.user.del_user(args.deluser)

    if ucheck:
        print("Successfully Deleted User")
    else:
        print("Username not found in DB")

# Test Authentication
elif args.testuser:
    passwd = getpass.getpass('Password:')
    phash = apisrv.user.authenticate_user(args.testuser, passwd)
    if phash:
        print("Successfully Authenticated")
    else:
        print("Authentication Failed")
else:
    parser.print_help()
    print()