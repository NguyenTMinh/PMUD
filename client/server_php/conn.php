<?php

// Connect to the MySQL database
$hostname = "localhost";
$username = "root";
$password = "";
$database = "traffic_sign";

$conn = mysqli_connect($hostname, $username, $password, $database);

// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
