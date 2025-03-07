<?php
// Database connection parameters
$servername = "localhost"; // Change this to your database server name if it's not localhost
$username = "root"; // Change this to your database username
$password = ""; // Change this to your database password
$database = "Daniel_Lunsford"; // Change this to your database name

// Create connection
$conn = mysqli_connect($servername, $username, $password,$database);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

?>