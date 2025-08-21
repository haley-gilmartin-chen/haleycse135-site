#!/usr/bin/php
<?php
print "Cache-Control: no-cache\n";
print "Content-type: text/html\n\n";
$body = stream_get_contents(STDIN);
parse_str($body, $params);
echo "<!DOCTYPE html><html><head><title>POST Request Echo</title></head><body><h1 align='center'>POST Request Echo</h1><hr>";
echo "<b>Message Body:</b><br/>\n<ul>\n";
foreach($params as $k=>$v){
  $k = htmlspecialchars($k, ENT_QUOTES, 'UTF-8');
  $v = htmlspecialchars($v, ENT_QUOTES, 'UTF-8');
  echo "<li>$k = $v</li>\n";
}
echo "</ul></body></html>";
