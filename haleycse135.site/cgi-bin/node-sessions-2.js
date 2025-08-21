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
    const name = req.session.username;

    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.write('<html>');
    res.write('<head><title>Node.js Sessions</title></head>');
    res.write('<body>');
    res.write('<h1>Node.js Sessions Page 2</h1>');
    
    if (name) {
        res.write(`<p><b>Name:</b> ${name}</p>`);
    } else {
        res.write('<p><b>Name:</b> You do not have a name set</p>');
    }
    
    res.write('<br/><br/>');
    res.write('<a href="/cgi-bin/node-sessions-1.js">Session Page 1</a><br/>');
    res.write('<a href="/nodejs-cgiform.html">Node.js CGI Form</a><br />');
    res.write('<form style="margin-top:30px" action="/cgi-bin/node-destroy-session.js" method="get">');
    res.write('<button type="submit">Destroy Session</button>');
    res.write('</form>');
    res.write('</body></html>');
    res.end();
});

const server = http.createServer(app);
server.listen(0);