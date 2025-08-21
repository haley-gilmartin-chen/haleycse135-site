#!/usr/bin/python3
import os
import sys
import http.cookies
from urllib.parse import parse_qs, unquote_plus

print("Cache-Control: no-cache")

username = None
if os.environ.get('REQUEST_METHOD') == 'POST':
    content_length = int(os.environ.get('CONTENT_LENGTH', 0))
    post_data = sys.stdin.read(content_length)
    
    form_data = parse_qs(post_data)
    if 'username' in form_data:
        username = unquote_plus(form_data['username'][0].strip())

cookie = http.cookies.SimpleCookie()

if username:
    cookie['username'] = username
    cookie['username']['path'] = '/'
    print(cookie.output())
elif 'HTTP_COOKIE' in os.environ:
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
    <h1>Python Sessions Page 1</h1>""")

if username:
    print(f"    <p><b>Name:</b> {username}</p>")
else:
    print("    <p><b>Name:</b> You do not have a name set</p>")

print("""    <br/><br/>
    <a href="/cgi-bin/py-sessions-2.py">Session Page 2</a><br />
    <a href="/python-cgiform.html">Python CGI Form</a><br />
    <form style="margin-top:30px" action="/cgi-bin/py-destroy-session.py" method="get">
        <button type="submit">Destroy Session</button>
    </form>
</body>
</html>""")