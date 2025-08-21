#!/usr/bin/php
<?php
print "Cache-Control: no-cache\n";
print "Content-type: text/html\n\n";
echo "<!DOCTYPE html><html><head><title>GET Request Echo</title></head><body><h1 align='center'>GET Request Echo</h1><hr>";
$query = getenv('QUERY_STRING') ?: '';
echo "<b>Query String:</b> ".$query."<br/>\n";
parse_str($query, $params);
foreach($params as $k=>$v){
  $k = htmlspecialchars($k, ENT_QUOTES, 'UTF-8');
  $v = htmlspecialchars($v, ENT_QUOTES, 'UTF-8');
  echo "$k = $v<br/>\n";
}
echo "</body></html>";
