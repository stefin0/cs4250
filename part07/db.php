<?php
$host = "localhost";
$dbname = "local_test_database";
$username = "root";
$password = "new_password";

$dsn = "mysql:host=$host;dbname=$dbname;";
$pdo = new PDO($dsn, $username, $password);
?>
