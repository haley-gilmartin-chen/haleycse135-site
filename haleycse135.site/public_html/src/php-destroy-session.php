#!/usr/bin/php-cgi
<?php
header("Cache-Control: no-cache");
setcookie('username', '', time() - 3600, '/');
?>
<!DOCTYPE html>
<html>
<head>
    <title>PHP Session Destroyed</title>
</head>
<body>
    <h1>PHP Session Destroyed</h1>
    <a href="/cgi-bin/php-sessions-1.php">Back to Session Page 1</a><br />
    <a href="/cgi-bin/php-sessions-2.php">Back to Session Page 2</a><br />
    <a href="/php-cgiform.html">Back to Form</a>
    <a href="/">Back to home</a>
</body>
</html>