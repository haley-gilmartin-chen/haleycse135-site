#!/usr/bin/env node

function header(name, value){ process.stdout.write(name+": "+value+"\n"); }
header("Cache-Control","no-cache");
header("Content-type","text/html");
process.stdout.write("\n");

process.stdout.write(`<!DOCTYPE html><html><head><title>General Request Echo</title></head><body><h1 align="center">General Request Echo</h1><hr>`);
process.stdout.write(`<p><b>HTTP Protocol:</b> ${process.env.SERVER_PROTOCOL||''}</p>`);
process.stdout.write(`<p><b>HTTP Method:</b> ${process.env.REQUEST_METHOD||''}</p>`);
process.stdout.write(`<p><b>Query String:</b> ${process.env.QUERY_STRING||''}</p>`);

let body = '';
process.stdin.setEncoding('utf8');
process.stdin.on('data', chunk => body += chunk);
process.stdin.on('end', () => {
  process.stdout.write(`<p><b>Message Body:</b> ${body}</p>`);
  process.stdout.write(`</body></html>`);
});
