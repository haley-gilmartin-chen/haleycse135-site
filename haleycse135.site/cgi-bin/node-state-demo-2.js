#!/usr/bin/env node

function header(name, value){ process.stdout.write(name+": "+value+"\n"); }
header("Cache-Control","no-cache");
header("Content-type","text/html");

let body = '';
process.stdin.setEncoding('utf8');
process.stdin.on('data', chunk => body += chunk);
process.stdin.on('end', () => {
  process.stdout.write("\n");
  const params = {};
  body.split('&').filter(Boolean).forEach(pair => {
    const [k,v] = pair.split('=');
    params[decodeURIComponent(k)] = decodeURIComponent((v||'').replace(/\+/g,' '));
  });
  const name = params.username || '';
  // Echo cookie if present
  const cookie = process.env.HTTP_COOKIE || '';
  header("Set-Cookie", `NODE_NAME=${encodeURIComponent(name)}; Path=/; HttpOnly`);
  process.stdout.write(`<!DOCTYPE html><html><head><title>Node Sessions</title></head><body>`);
  process.stdout.write(`<h1>Node Sessions Page 2</h1>`);
  process.stdout.write(`<p><b>Name:</b> ${name ? name : 'You do not have a name set'}</p>`);
  process.stdout.write(`<p><b>Cookie:</b> ${cookie}</p>`);
  process.stdout.write(`<a href="/cgi-bin/node-state-demo-1.js">Back to Page 1</a>`);
  process.stdout.write(`</body></html>`);
});
