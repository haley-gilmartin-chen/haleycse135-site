#!/usr/bin/env node

function header(name, value){ process.stdout.write(name+": "+value+"\n"); }
header("Cache-Control","no-cache");
header("Content-type","application/json");
process.stdout.write("\n");

const ip = process.env.REMOTE_ADDR || "";
const now = new Date().toString();
const payload = { title: "Hello, Node!", heading: "Hello, Node!", message: "This page was generated with the Node.js runtime", time: now, IP: ip };
process.stdout.write(JSON.stringify(payload)+"\n");
