#!/usr/bin/php-cgi
<?php
session_start();
session_destroy();
header("Cache-Control: no-cache");
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
    <a href="/php-cgiform.html">Back to Form</a><br />
    <a href="/">Back to Home</a>
</body>
</html>