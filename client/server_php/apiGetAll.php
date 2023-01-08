
<?php 
        // Connect to the MySQL database
		include 'conn.php';
		
?>
<?php



// Execute the SELECT query
$sql = "SELECT * FROM traffic_signs";
$result = mysqli_query($conn, $sql);

// Iterate over the result set and create an array of data
$data = array();
while ($row = mysqli_fetch_assoc($result)) {
    $data[] = $row;
}

// Return the data as a JSON object
echo json_encode($data);

// Close the connection
mysqli_close($conn);

