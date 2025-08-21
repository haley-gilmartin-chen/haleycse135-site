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
    <a href="/cgi-bin/php-state-demo.php">Back to Session Page</a><br />
    <a href="/php-cgiform.html">Back to Form</a>
</body>
</html>
