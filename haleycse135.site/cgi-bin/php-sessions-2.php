<!-- /cgi-bin/php-sessions-2.php -->
<?php
session_name('CGISESSID');
session_start();

header('Cache-Control: no-cache');
header('Content-Type: text/html');

$name = $_SESSION['username'] ?? null;

$rawCookie = $_SERVER['HTTP_COOKIE'] ?? null;
?>
<!DOCTYPE html>
<html>
<head><title>PHP Sessions</title></head>
<body>
  <h1>PHP Sessions Page 2</h1>

  <?php if (!empty($name)): ?>
    <p><b>Name:</b> <?= htmlspecialchars($name, ENT_QUOTES) ?></p>
  <?php else: ?>
    <p><b>Name:</b> You do not have a name set</p>
  <?php endif; ?>

  <br/><br/>
  <table>
    <tr><td>Cookie (raw):</td><td><?= htmlspecialchars($rawCookie ?? 'None', ENT_QUOTES) ?></td></tr>
  </table>

  <br/>
  <a href="/cgi-bin/php-sessions-1.php">Session Page 1</a><br/>
  <a href="/php-cgiform.html">PHP CGI Form</a><br/><br/>

  <form action="/cgi-bin/php-destroy-session.php" method="get">
    <button type="submit">Destroy Session</button>
  </form>
</body>
</html>