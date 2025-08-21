#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const SESS_DIR = '/tmp/node-sessions';

function header(name, value){ process.stdout.write(name+": "+value+"\n"); }
function endHeaders(){ process.stdout.write("\n"); }

// Ensure session dir
try { fs.mkdirSync(SESS_DIR, { recursive: true }); } catch (e) {}

// Parse cookies
const cookieHdr = process.env.HTTP_COOKIE || '';
const cookies = Object.fromEntries(cookieHdr.split(';').map(s=>s.trim()).filter(Boolean).map(p=>{
  const idx = p.indexOf('=');
  if (idx === -1) return [p, ''];
  return [p.slice(0, idx), decodeURIComponent(p.slice(idx+1))];
}));
let sid = cookies['NODE_SID'];
if (!sid) {
  sid = Math.random().toString(36).slice(2);
  header('Set-Cookie', `NODE_SID=${sid}; Path=/; HttpOnly`);
}

const method = process.env.REQUEST_METHOD || 'GET';
header('Cache-Control','no-cache');
header('Content-type','text/html');
endHeaders();

const sessFile = path.join(SESS_DIR, sid + '.txt');

function readName(){ try { return fs.readFileSync(sessFile, 'utf8'); } catch(e){ return ''; } }
function writeName(name){ try { fs.writeFileSync(sessFile, name, 'utf8'); } catch(e){} }

if (method === 'POST') {
  let body = '';
  process.stdin.setEncoding('utf8');
  process.stdin.on('data', chunk => body += chunk);
  process.stdin.on('end', () => {
    const params = {};
    body.split('&').filter(Boolean).forEach(pair => {
      const [k,v] = pair.split('=');
      params[decodeURIComponent(k)] = decodeURIComponent((v||'').replace(/\+/g,' '));
    });
    const name = params.username || '';
    if (name) writeName(name);
    render();
  });
} else {
  render();
}

function render(){
  const saved = readName();
  process.stdout.write(`<!DOCTYPE html><html><head><title>Node Sessions</title></head><body>`);
  process.stdout.write(`<h1>Node Sessions</h1>`);
  process.stdout.write(`<p><b>Name:</b> ${saved ? saved : 'You do not have a name set'}</p>`);
  process.stdout.write(`<form action="/cgi-bin/node-state-demo.js" method="POST" style="margin-top:16px">`);
  process.stdout.write(`Name: <input type="text" name="username" /> <button type="submit">Save</button>`);
  process.stdout.write(`</form>`);
  process.stdout.write(`</body></html>`);
}
