#!/usr/bin/env python3
import os, time, json

print("Cache-Control: no-cache")
print("Content-type: application/json\n")

now = time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
ip = os.environ.get("REMOTE_ADDR", "unknown")

payload = {
  "title": "Hello, Python!",
  "heading": "Hello, Python!",
  "message": "This page was generated with the Python programming language",
  "time": now,
  "IP": ip
}

print(json.dumps(payload))
