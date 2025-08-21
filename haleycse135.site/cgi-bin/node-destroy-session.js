#!/usr/bin/env node
const http = require('http');
const session = require('express-session');
const express = require('express');

const app = express();

app.use(session({
    name: 'CGISESSID',
    secret: 'your-secret-key',
    resave: false,
    saveUninitialized: true,
    cookie: { secure: false }
}));

app.get('/', (req, res) => {
    req.session.destroy();
    
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.write('<html>');
    res.write('<head><title>Node.js Session Destroyed</title></head>');
    res.write('<body>');
    res.write('<h1>Session Destroyed</h1>');
    res.write('<a href="/nodejs-cgiform.html">Back to the Node.js CGI Form</a><br />');
    res.write('<a href="/cgi-bin/node-sessions-1.js">Back to Page 1</a><br />');
    res.write('<a href="/cgi-bin/node-sessions-2.js">Back to Page 2</a>');
    res.write('</body></html>');
    res.end();
});

const server = http.createServer(app);
server.listen(0);
