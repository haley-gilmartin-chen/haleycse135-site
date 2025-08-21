#!/usr/bin/env python3
import sys, os, urllib.parse

print("Cache-Control: no-cache")
print("Content-type: text/html\n")

print("""
<!DOCTYPE html>
<html><head><title>POST Request Echo</title></head>
<body><h1 align="center">POST Request Echo</h1>
<hr>
""")

length = int(os.environ.get('CONTENT_LENGTH', '0') or 0)
body = sys.stdin.read(length) if length > 0 else ''

print("<b>Message Body:</b><br />")
print("<ul>")

pairs = urllib.parse.parse_qs(body)
for key, values in pairs.items():
    for value in values:
        print(f"<li>{key} = {value}</li>")

print("</ul>")
print("</body></html>")
