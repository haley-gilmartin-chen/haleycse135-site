<!-- /cgi-bin/php-sessions-1.php -->
<?php
session_name('CGISESSID');
session_start();

header('Cache-Control: no-cache');
header('Content-Type: text/html');

$name = $_SESSION['username'] ?? null;
if (isset($_REQUEST['username']) && $_REQUEST['username'] !== '') {
    $name = $_REQUEST['username'];
    $_SESSION['username'] = $name;
}
?>
<!DOCTYPE html>
<html>
<head><title>PHP Sessions</title></head>
<body>
  <h1>PHP Sessions Page 1</h1>

  <?php if (!empty($name)): ?>
    <p><b>Name:</b> <?= htmlspecialchars($name, ENT_QUOTES) ?></p>
  <?php else: ?>
    <p><b>Name:</b> You do not have a name set</p>
  <?php endif; ?>

  <br/><br/>

  <form method="get" action="/cgi-bin/php-sessions-1.php">
    <input name="username" placeholder="Enter your name" />
    <button type="submit">Save Name (Session)</button>
  </form>

  <br/><br/>
  <a href="/cgi-bin/php-sessions-2.php">Session Page 2</a><br/>
  <a href="/php-cgiform.html">PHP CGI Form</a><br/>

  <form style="margin-top:30px" action="/cgi-bin/php-destroy-session.php" method="get">
    <button type="submit">Destroy Session</button>
  </form>
</body>
</html>