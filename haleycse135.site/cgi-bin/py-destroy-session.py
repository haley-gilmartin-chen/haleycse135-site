#!/usr/bin/python3
import http.cookies
from datetime import datetime, timedelta

print("Cache-Control: no-cache")

cookie = http.cookies.SimpleCookie()
cookie['username'] = ''
cookie['username']['expires'] = (datetime.now() - timedelta(days=1)).strftime('%a, %d %b %Y %H:%M:%S GMT')
cookie['username']['path'] = '/'
print(cookie.output())

print("Content-type: text/html\n")

print("""<!DOCTYPE html>
<html>
<head>
    <title>Python Session Destroyed</title>
</head>
<body>
    <h1>Python Session Destroyed</h1>
    <a href="/cgi-bin/py-sessions-1.py">Back to Page 1</a><br />
    <a href="/cgi-bin/py-sessions-2.py">Back to Page 2</a><br />
    <a href="/python-cgiform.html">Back to Form</a><br />
    <a href="/">Back to Home</a>
</body>
</html>""")