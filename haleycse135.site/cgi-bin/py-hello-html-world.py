#!/usr/bin/env python3
import os, time

print("Cache-Control: no-cache")
print("Content-type: text/html\n")

now = time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
ip = os.environ.get("REMOTE_ADDR", "unknown")

print("""
<!DOCTYPE html>
<html><head><title>Hello, Python!</title></head>
<body>
  <h1>Haley Chen</h1>
  <h1>Hello, Python!</h1>
  <p>This page was generated with the Python programming language</p>
  <p>Current Time: {now}</p>
  <p>Your IP Address: {ip}</p>
</body></html>
""".format(now=now, ip=ip))
