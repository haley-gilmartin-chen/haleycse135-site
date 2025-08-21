#!/usr/bin/env node

function header(name, value){ process.stdout.write(name+": "+value+"\n"); }
header("Cache-Control","no-cache");
header("Content-type","text/html");
process.stdout.write("\n");

process.stdout.write(`<!DOCTYPE html><html><head><title>GET Request Echo</title></head><body><h1 align="center">GET Request Echo</h1><hr>`);
const qs = process.env.QUERY_STRING || "";
process.stdout.write(`<b>Query String:</b> ${qs}<br/>\n`);
const params = {};
qs.split('&').filter(Boolean).forEach(pair => {
  const [k,v] = pair.split('=');
  params[decodeURIComponent(k)] = decodeURIComponent((v||'').replace(/\+/g,' '));
});
Object.keys(params).forEach(k => {
  process.stdout.write(`${k} = ${params[k]}<br/>\n`);
});
process.stdout.write(`</body></html>`);
