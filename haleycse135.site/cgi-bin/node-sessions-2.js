#!/usr/bin/node

process.stdout.write("Cache-Control: no-cache\n");
process.stdout.write("Content-type: text/html\n\n");

let cookies = {};

if (process.env.HTTP_COOKIE) {
    cookies = process.env.HTTP_COOKIE.split(';').reduce((acc, cookie) => {
        const [key, value] = cookie.trim().split('=');
        acc[key] = value;
        return acc;
    }, {});
}

process.stdout.write(`
    <html>
    <head><title>NodeJS Sessions</title></head>
    <body>
    <h1>NodeJS Sessions Page 2</h1>
    ${cookies.username ? 
        `<p><b>Name:</b> ${cookies.username}</p>` :
        '<p><b>Name:</b> You do not have a name set</p>'
    }
    <br/><br/>
    <a href="/cgi-bin/node-sessions-1.js">Session Page 1</a><br />
    <a href="/nodejs-cgiform.html">NodeJS CGI Form</a><br />
    <form style="margin-top:30px" action="/cgi-bin/node-destroy-session.js" method="get">
    <button type="submit">Destroy Session</button>
    </form>
    </body>
    </html>
`);