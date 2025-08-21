#!/usr/bin/env python3
import os, sys, http.cookies, urllib.parse

def print_headers(set_cookie=None, content_type="text/html"):
    print("Cache-Control: no-cache")
    if set_cookie:
        print(set_cookie.OutputString())
    print(f"Content-type: {content_type}\n")

def main():
    method = os.environ.get("REQUEST_METHOD", "GET").upper()
    cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE", ""))
    name_cookie = cookie.get("username")
    current_name = name_cookie.value if name_cookie else ""

    if method == "POST":
        length = int(os.environ.get('CONTENT_LENGTH', '0') or 0)
        body = sys.stdin.read(length) if length > 0 else ''
        fields = urllib.parse.parse_qs(body)
        new_name = fields.get('username', [""])[0]
        c = http.cookies.SimpleCookie()
        c['username'] = new_name
        c['username']['path'] = '/'
        print_headers(set_cookie=c)
        current_name = new_name
    else:
        # GET - possibly destroy
        qs = os.environ.get('QUERY_STRING', '')
        params = urllib.parse.parse_qs(qs)
        if 'destroy' in params:
            c = http.cookies.SimpleCookie()
            c['username'] = 'deleted'
            c['username']['path'] = '/'
            c['username']['expires'] = 'Thu, 01 Jan 1970 00:00:00 GMT'
            print_headers(set_cookie=c)
            current_name = ""
        else:
            print_headers()

    print("""
<!DOCTYPE html>
<html><head><title>Python State Demo</title></head>
<body>
  <h1>Python State Demo</h1>
  <table>
    <tr><td>Cookie:</td><td>{cookie_val}</td></tr>
  </table>
  <br/>
  <form method="post" action="/cgi-bin/py-state-demo.py">
    Name: <input type="text" name="username" value="{cookie_val}" />
    <button type="submit">Set Name</button>
  </form>
  <br/>
  <a href="/cgi-bin/py-state-demo.py">State Page (refresh)</a><br/>
  <a href="/cgi-bin/py-state-demo.py?destroy=1">Destroy State</a>
</body></html>
""".format(cookie_val=(current_name or 'None')))

if __name__ == "__main__":
    main()
