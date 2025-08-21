#!/usr/bin/php-cgi
<?php
header("Cache-Control: no-cache");

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['username'])) {
    setcookie('username', $_POST['username'], 0, '/');
    $username = $_POST['username'];
} else {
    $username = isset($_COOKIE['username']) ? $_COOKIE['username'] : null;
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>PHP Sessions</title>
</head>
<body>
    <h1>PHP Sessions Page 1</h1>
    <?php if ($username): ?>
        <p><b>Name:</b> <?php echo htmlspecialchars($username); ?></p>
    <?php else: ?>
        <p><b>Name:</b> You do not have a name set</p>
    <?php endif; ?>
    <br/><br/>
    <a href="/cgi-bin/php-sessions-2.php">Session Page 2</a><br />
    <a href="/php-cgiform.html">PHP CGI Form</a><br />
    <form style="margin-top:30px" action="/cgi-bin/php-destroy-session.php" method="get">
        <button type="submit">Destroy Session</button>
    </form>
</body>
</html>