#!/usr/bin/env node

function header(name, value){ process.stdout.write(name+": "+value+"\n"); }
header("Cache-Control","no-cache");
header("Content-type","text/html");
process.stdout.write("\n");

process.stdout.write(`<!DOCTYPE html><html><head><title>Environment Variables</title></head><body><h1 align="center">Environment Variables</h1><hr>`);
Object.keys(process.env).sort().forEach(k => {
  process.stdout.write(`<b>${k}:</b> ${process.env[k]}<br/>\n`);
});
process.stdout.write(`</body></html>`);
