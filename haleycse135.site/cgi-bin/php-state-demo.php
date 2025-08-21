#!/usr/bin/php
<?php
print "Cache-Control: no-cache\n";
print "Content-type: text/html\n\n";
$cookie = $_COOKIE['PHP_SID'] ?? '';
if (!$cookie) {
  $cookie = bin2hex(random_bytes(8));
  header("Set-Cookie: PHP_SID=$cookie; Path=/; HttpOnly");
}
$sess = sys_get_temp_dir()."/php-sess-".$cookie;
if ($_SERVER['REQUEST_METHOD']==='POST') {
  $name = $_POST['username'] ?? '';
  file_put_contents($sess, $name);
}
$name = @file_get_contents($sess) ?: '';
echo "<!DOCTYPE html><html><head><title>PHP Sessions</title></head><body>";
echo "<h1>PHP Sessions</h1>";
echo "<p><b>Name:</b> ".($name?htmlspecialchars($name, ENT_QUOTES, 'UTF-8'):'You do not have a name set')."</p>";
echo "<form action='/cgi-bin/php-state-demo.php' method='POST' style='margin-top:16px'>";
echo "Name: <input type='text' name='username' /> <button type='submit'>Save</button>";
echo "</form>";
echo "</body></html>";
