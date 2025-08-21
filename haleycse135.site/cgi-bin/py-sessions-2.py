#!/usr/bin/env python3
import cgi
import cgitb
import os
from http import cookies
import sys
import json

cgitb.enable()

def load_session():
    cookie = cookies.SimpleCookie()
    if 'HTTP_COOKIE' in os.environ:
        cookie.load(os.environ['HTTP_COOKIE'])
    if 'session' in cookie:
        try:
            with open(f"/tmp/{cookie['session'].value}.json", 'r') as f:
                return json.load(f)
        except:
            pass
    return {}

# Get session data
session_data = load_session()
name = session_data.get('username', '')

print("Content-Type: text/html")
print()

print("""
<html>
<head>
    <title>Python Sessions</title>
</head>
<body>
    <h1>Python Sessions Page 2</h1>""")

if name:
    print(f"<p><b>Name:</b> {name}</p>")
else:
    print("<p><b>Name:</b> You do not have a name set</p>")

print("""
    <br/><br/>
    <a href="/cgi-bin/py-state-demo-1.py">Session Page 1</a><br/>
    <a href="/python-cgiform.html">Python CGI Form</a><br />
    <form style="margin-top:30px" action="/cgi-bin/py-destroy-session.py" method="get">
        <button type="submit">Destroy Session</button>
    </form>
</body>
</html>""")
