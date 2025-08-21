#!/usr/bin/php
<?php
print "Cache-Control: no-cache\n";
print "Content-type: text/html\n\n";
$ip = getenv('REMOTE_ADDR');
$date = date('r');
print "<!DOCTYPE html><html><head><title>Hello, PHP!</title></head><body>";
print "<h1>Hello, PHP!</h1>";
print "<p>This page was generated with the PHP runtime</p>";
print "<p>Current Time: $date</p>";
print "<p>Your IP Address: $ip</p>";
print "</body></html>";
