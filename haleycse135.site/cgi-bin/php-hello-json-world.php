#!/usr/bin/php
<?php
header("Cache-Control: no-cache");
header("Content-type: application/json");
$ip = getenv('REMOTE_ADDR');
$date = date('r');
echo json_encode([
  'title' => 'Hello, PHP!',
  'heading' => 'Hello, PHP!',
  'message' => 'This page was generated with the PHP runtime',
  'time' => $date,
  'IP' => $ip
]);
