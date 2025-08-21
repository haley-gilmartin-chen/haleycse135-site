#!/usr/bin/env node

function header(name, value){ process.stdout.write(name+": "+value+"\n"); }
header("Cache-Control","no-cache");
header("Content-type","text/html");
process.stdout.write("\n");

// Using cookie for session id
const sid = (Math.random().toString(36).slice(2));
header("Set-Cookie", `NODE_SID=${sid}; Path=/; HttpOnly`);
process.stdout.write(`<!DOCTYPE html><html><head><title>Node Sessions</title></head><body>`);
process.stdout.write(`<h1>Node Sessions Page 1</h1>`);
process.stdout.write(`<form action="/cgi-bin/node-state-demo-2.js" method="POST">`);
process.stdout.write(`Name: <input type="text" name="username" />`);
process.stdout.write(`<input type="submit" value="Submit" />`);
process.stdout.write(`</form>`);
process.stdout.write(`</body></html>`);
