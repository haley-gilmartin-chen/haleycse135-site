#!/usr/bin/php-cgi
<?php
session_start();

header("Cache-Control: no-cache");

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['username'])) {
    $_SESSION['username'] = $_POST['username'];
}

?>
<!DOCTYPE html>
<html>
<head>
    <title>PHP Sessions</title>
</head>
<body>
    <h1>PHP Sessions Page</h1>
    <?php if (isset($_SESSION['username'])): ?>
        <p><b>Name:</b> <?php echo htmlspecialchars($_SESSION['username']); ?></p>
    <?php else: ?>
        <p><b>Name:</b> You do not have a name set</p>
    <?php endif; ?>
    <br/><br/>
    <a href="/php-cgiform.html">PHP CGI Form</a><br />
    <form style="margin-top:30px" action="/cgi-bin/php-destroy-session.php" method="get">
        <button type="submit">Destroy Session</button>
    </form>
</body>
</html>
