#!/usr/bin/php
<?php
print "Cache-Control: no-cache\n";
print "Content-type: text/html\n\n";
echo "<!DOCTYPE html><html><head><title>Environment Variables</title></head><body><h1 align='center'>Environment Variables</h1><hr>";
ksort($_SERVER);
foreach($_SERVER as $k=>$v){
  $v = htmlspecialchars((string)$v, ENT_QUOTES, 'UTF-8');
  echo "<b>$k:</b> $v<br/>\n";
}
echo "</body></html>";
