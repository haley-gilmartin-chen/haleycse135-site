#!/usr/bin/php
<?php
print "Cache-Control: no-cache\n";
print "Content-type: text/html\n\n";
$method = getenv('REQUEST_METHOD');
$query = getenv('QUERY_STRING');
$protocol = getenv('SERVER_PROTOCOL');
$body = stream_get_contents(STDIN);
echo "<!DOCTYPE html><html><head><title>General Request Echo</title></head><body><h1 align='center'>General Request Echo</h1><hr>";
echo "<p><b>HTTP Protocol:</b> $protocol</p>";
echo "<p><b>HTTP Method:</b> $method</p>";
echo "<p><b>Query String:</b> $query</p>";
echo "<p><b>Message Body:</b> ".htmlspecialchars($body, ENT_QUOTES, 'UTF-8')."</p>";
echo "</body></html>";
