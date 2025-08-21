#!/usr/bin/env node
const http = require('http');
const querystring = require('querystring');
const session = require('express-session');
const express = require('express');

const app = express();

app.use(session({
    secret: 'your-secret-key',
    resave: false,
    saveUninitialized: true,
    cookie: { secure: false }
}));

app.use(express.urlencoded({ extended: true }));

app.post('/', (req, res) => {
    const name = req.session.username || req.body.username;
    req.session.username = name;

    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.write('<html>');
    res.write('<head><title>Node.js Sessions</title></head>');
    res.write('<body>');
    res.write('<h1>Node.js Sessions Page 1</h1>');
    
    if (name) {
        res.write(`<p><b>Name:</b> ${name}</p>`);
    } else {
        res.write('<p><b>Name:</b> You do not have a name set</p>');
    }
    
    res.write('<br/><br/>');
    res.write('<a href="/cgi-bin/node-state-demo-2.js">Session Page 2</a><br/>');
    res.write('<a href="/node-cgiform.html">Node.js CGI Form</a><br />');
    res.write('<form style="margin-top:30px" action="/cgi-bin/node-destroy-session.js" method="get">');
    res.write('<button type="submit">Destroy Session</button>');
    res.write('</form>');
    res.write('</body></html>');
    res.end();
});

const server = http.createServer(app);
server.listen(0);