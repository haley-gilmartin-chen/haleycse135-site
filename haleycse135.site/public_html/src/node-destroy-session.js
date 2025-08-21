#!/usr/bin/node

process.stdout.write("Cache-Control: no-cache\n");
process.stdout.write("Set-Cookie: username=; expires=Thu, 01 Jan 1970 00:00:00 GMT\n");
process.stdout.write("Content-type: text/html\n\n");

process.stdout.write(`
    <html>
    <head><title>NodeJS Session Destroyed</title></head>
    <body>
    <h1>NodeJS Session Destroyed</h1>
    <a href="/cgi-bin/node-state-demo.js">Back to Session Page</a><br />
    <a href="/node-cgiform.html">Back to Form</a>
    </body>
    </html>
`);
