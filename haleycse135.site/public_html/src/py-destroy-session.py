#!/usr/bin/python3
import http.cookies

print("Cache-Control: no-cache")
cookie = http.cookies.SimpleCookie()
cookie['username'] = ''
cookie['username']['expires'] = 'Thu, 01 Jan 1970 00:00:00 GMT'
print(cookie.output())
print("Content-type: text/html\n")

print("""
<html>
<head><title>Python Session Destroyed</title></head>
<body>
<h1>Python Session Destroyed</h1>
<a href="/cgi-bin/py-state-demo.py">Back to Session Page</a><br />
<a href="/python-cgiform.html">Back to Form</a>
</body>
</html>
""")
