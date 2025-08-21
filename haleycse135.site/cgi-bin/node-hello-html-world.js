#!/usr/bin/env node

function header(name, value){ process.stdout.write(name+": "+value+"\n"); }
header("Cache-Control","no-cache");
header("Content-type","text/html");
process.stdout.write("\n");

const ip = process.env.REMOTE_ADDR || "";
const now = new Date().toString();
process.stdout.write(`<!DOCTYPE html><html><head><title>Hello, Node!</title></head><body>`);
process.stdout.write(`<h1>Hello, Node!</h1>`);
process.stdout.write(`<p>This page was generated with the Node.js runtime</p>`);
process.stdout.write(`<p>Current Time: ${now}</p>`);
process.stdout.write(`<p>Your IP Address: ${ip}</p>`);
process.stdout.write(`</body></html>`);
