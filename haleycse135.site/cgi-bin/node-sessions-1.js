#!/usr/bin/node

const querystring = require('querystring');

process.stdout.write("Cache-Control: no-cache\n");

let username = null;
let cookies = {};

// Parse cookies
if (process.env.HTTP_COOKIE) {
    cookies = process.env.HTTP_COOKIE.split(';').reduce((acc, cookie) => {
        const [key, value] = cookie.trim().split('=');
        acc[key] = value;
        return acc;
    }, {});
}

// Handle POST data
if (process.env.REQUEST_METHOD === 'POST') {
    let body = '';
    process.stdin.on('data', chunk => {
        body += chunk.toString();
    });
    process.stdin.on('end', () => {
        const post = querystring.parse(body);
        if (post.username) {
            process.stdout.write(`Set-Cookie: username=${post.username}\n`);
            username = post.username;
        }
        outputPage(username || cookies.username);
    });
} else {
    outputPage(cookies.username);
}

function outputPage(username) {
    process.stdout.write("Content-type: text/html\n\n");
    process.stdout.write(`
        <html>
        <head><title>NodeJS Sessions</title></head>
        <body>
        <h1>NodeJS Sessions Page 1</h1>
        ${username ? 
            `<p><b>Name:</b> ${username}</p>` :
            '<p><b>Name:</b> You do not have a name set</p>'
        }
        <br/><br/>
        <a href="/cgi-bin/node-sessions-2.js">Session Page 2</a><br />
        <a href="/nodejs-cgiform.html">NodeJS CGI Form</a><br />
        <form style="margin-top:30px" action="/cgi-bin/node-destroy-session.js" method="get">
        <button type="submit">Destroy Session</button>
        </form>
        </body>
        </html>
    `);
}
