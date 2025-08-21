#!/usr/bin/python3
import os
import http.cookies

print("Cache-Control: no-cache")

username = None
if 'HTTP_COOKIE' in os.environ:
    cookie = http.cookies.SimpleCookie()
    cookie.load(os.environ['HTTP_COOKIE'])
    if 'username' in cookie:
        username = cookie['username'].value

print("Content-type: text/html\n")

print("""<!DOCTYPE html>
<html>
<head>
    <title>Python Sessions</title>
</head>
<body>
    <h1>Python Sessions Page 2</h1>""")

if username:
    print(f"    <p><b>Name:</b> {username}</p>")
else:
    print("    <p><b>Name:</b> You do not have a name set</p>")

print("""    <br/><br/>
    <a href="/cgi-bin/py-sessions-1.py">Session Page 1</a><br />
    <a href="/python-cgiform.html">Python CGI Form</a><br />
    <form style="margin-top:30px" action="/cgi-bin/py-destroy-session.py" method="get">
        <button type="submit">Destroy Session</button>
    </form>
</body>
</html>""")