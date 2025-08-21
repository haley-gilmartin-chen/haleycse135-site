#!/usr/bin/env python3
import os, sys, http.cookies

print("Cache-Control: no-cache")
print("Content-type: text/html\n")

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE", ""))
name = cookie.get("username")
name_val = name.value if name else ""

print("""
<!DOCTYPE html>
<html><head><title>Python Sessions</title></head>
<body>
<h1>Python Sessions Page 1</h1>
<form action="/cgi-bin/py-state-1.py" method="post">
  Name: <input type="text" name="username" value="{name}" />
  <button type="submit">Set Name</button>
</form>
<br/>
<a href="/cgi-bin/py-state-2.py">Session Page 2</a>
</body></html>
""".format(name=name_val))
