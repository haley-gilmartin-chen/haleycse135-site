#!/usr/bin/python3
import os
import sys
import http.cookies
from urllib.parse import parse_qs, unquote_plus

# Print headers first
print("Cache-Control: no-cache")

# Get form data
username = None
if os.environ.get('REQUEST_METHOD') == 'POST':
    # Read POST data
    content_length = int(os.environ.get('CONTENT_LENGTH', 0))
    post_data = sys.stdin.read(content_length)
    
    # Parse form data
    form_data = parse_qs(post_data)
    if 'username' in form_data:
        # Clean up the username value
        username = unquote_plus(form_data['username'][0].strip())

# Create or get cookie
cookie = http.cookies.SimpleCookie()

if username:
    # Set the cookie if username was submitted
    cookie['username'] = username
    cookie['username']['path'] = '/'  # Make cookie available for all paths
    print(cookie.output())
elif 'HTTP_COOKIE' in os.environ:
    # Try to load existing cookie
    cookie.load(os.environ['HTTP_COOKIE'])
    if 'username' in cookie:
        username = cookie['username'].value

# Print content type header
print("Content-type: text/html\n")

# Print HTML
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