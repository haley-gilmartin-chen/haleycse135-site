#!/usr/bin/python3
import os
import cgi
import http.cookies
from urllib.parse import parse_qs

print("Cache-Control: no-cache")

# Get form data
form = cgi.FieldStorage()
username = form.getvalue('username')

# Create or get cookie
cookie = http.cookies.SimpleCookie()
if username:
    cookie['username'] = username
    print(cookie.output())
elif 'HTTP_COOKIE' in os.environ:
    cookie.load(os.environ['HTTP_COOKIE'])
    username = cookie.get('username', None)
    if username:
        username = username.value

print("Content-type: text/html\n")

print("""
<html>
<head><title>Python Sessions</title></head>
<body>
<h1>Python Sessions Page</h1>
""")

if username:
    print(f"<p><b>Name:</b> {username}</p>")
else:
    print("<p><b>Name:</b> You do not have a name set</p>")

print("""
<br/><br/>
<a href="/python-cgiform.html">Python CGI Form</a><br />
<form style="margin-top:30px" action="/cgi-bin/py-destroy-session.py" method="get">
<button type="submit">Destroy Session</button>
</form>
</body>
</html>
""")
