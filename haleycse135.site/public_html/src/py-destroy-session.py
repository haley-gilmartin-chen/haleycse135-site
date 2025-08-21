#!/usr/bin/python3
import http.cookies
from datetime import datetime, timedelta

# Print headers first
print("Cache-Control: no-cache")

# Create cookie with expired date to delete it
cookie = http.cookies.SimpleCookie()
cookie['username'] = ''
cookie['username']['expires'] = (datetime.now() - timedelta(days=1)).strftime('%a, %d %b %Y %H:%M:%S GMT')
cookie['username']['path'] = '/'  # Important: match the path used when setting
print(cookie.output())

# Print content type header
print("Content-type: text/html\n")

# Print HTML
print("""<!DOCTYPE html>
<html>
<head>
    <title>Python Session Destroyed</title>
</head>
<body>
    <h1>Python Session Destroyed</h1>
    <a href="/cgi-bin/py-sessions-1.py">Back to Session Page 1</a><br />
    <a href="/cgi-bin/py-sessions-2.py">Back to Session Page 2</a><br />
    <a href="/python-cgiform.html">Back to Form</a>
    <a href="/">Back to home</a>
</body>
</html>""")