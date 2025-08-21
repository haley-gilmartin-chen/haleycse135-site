#!/usr/bin/env python3
import cgi
import cgitb
import os
from http import cookies
import sys
import json
from urllib.parse import parse_qs

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

def save_session(session_data):
    cookie = cookies.SimpleCookie()
    if 'HTTP_COOKIE' in os.environ:
        cookie.load(os.environ['HTTP_COOKIE'])
    if 'session' not in cookie:
        import uuid
        session_id = str(uuid.uuid4())
        cookie['session'] = session_id
    with open(f"/tmp/{cookie['session'].value}.json", 'w') as f:
        json.dump(session_data, f)
    return cookie

# Get form data
form = cgi.FieldStorage()
session_data = load_session()

# Update session if username is provided
if 'username' in form:
    session_data['username'] = form.getvalue('username')

# Save session and get cookie
cookie = save_session(session_data)

print("Content-Type: text/html")
print(cookie.output())
print()

name = session_data.get('username', '')

print("""
<html>
<head>
    <title>Python Sessions</title>
</head>
<body>
    <h1>Python Sessions Page 1</h1>""")

if name:
    print(f"<p><b>Name:</b> {name}</p>")
else:
    print("<p><b>Name:</b> You do not have a name set</p>")

print("""
    <br/><br/>
    <a href="/cgi-bin/py-state-demo-2.py">Session Page 2</a><br/>
    <a href="/python-cgiform.html">Python CGI Form</a><br />
    <form style="margin-top:30px" action="/cgi-bin/py-destroy-session.py" method="get">
        <button type="submit">Destroy Session</button>
    </form>
</body>
</html>""")
