#!/usr/bin/env python3
import sys, os

print("Cache-Control: no-cache")
print("Content-type: text/html\n")

print("""
<!DOCTYPE html>
<html><head><title>General Request Echo</title></head>
<body><h1 align="center">General Request Echo</h1>
<hr>
""")

print(f"<p><b>HTTP Protocol:</b> {os.environ.get('SERVER_PROTOCOL','')}</p>")
print(f"<p><b>HTTP Method:</b> {os.environ.get('REQUEST_METHOD','')}</p>")
print(f"<p><b>Query String:</b> {os.environ.get('QUERY_STRING','')}</p>")

length = int(os.environ.get('CONTENT_LENGTH', '0') or 0)
body = sys.stdin.read(length) if length > 0 else ''
print(f"<p><b>Message Body:</b> {body}</p>")

print("</body></html>")
