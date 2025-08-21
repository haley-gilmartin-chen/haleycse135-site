#!/usr/bin/env python3
import os, urllib.parse

print("Cache-Control: no-cache")
print("Content-type: text/html\n")

print("""
<!DOCTYPE html>
<html><head><title>GET Request Echo</title></head>
<body><h1 align="center">GET Request Echo</h1>
<hr>
""")

qs = os.environ.get('QUERY_STRING', '')
print(f"<b>Query String:</b> {qs}<br />")

pairs = urllib.parse.parse_qs(qs)
for key, values in pairs.items():
    for value in values:
        print(f"{key} = {value}<br/>")

print("</body></html>")
