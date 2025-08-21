#!/usr/bin/env node

function header(name, value){ process.stdout.write(name+": "+value+"\n"); }
header("Cache-Control","no-cache");
header("Content-type","text/html");
process.stdout.write("\n");

let body = '';
process.stdin.setEncoding('utf8');
process.stdin.on('data', chunk => body += chunk);
process.stdin.on('end', () => {
  process.stdout.write(`<!DOCTYPE html><html><head><title>POST Request Echo</title></head><body><h1 align="center">POST Request Echo</h1><hr>`);
  process.stdout.write(`<b>Message Body:</b><br/>\n<ul>\n`);
  const params = {};
  body.split('&').filter(Boolean).forEach(pair => {
    const [k,v] = pair.split('=');
    params[decodeURIComponent(k)] = decodeURIComponent((v||'').replace(/\+/g,' '));
  });
  Object.keys(params).forEach(k => {
    process.stdout.write(`<li>${k} = ${params[k]}</li>\n`);
  });
  process.stdout.write(`</ul></body></html>`);
});
