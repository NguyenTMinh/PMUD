<?php 
$base64Image  = $_POST['img'];
$imageData = base64_decode(preg_replace('#^data:image/\w+;base64,#i', '', $base64Image));
$randomNumber = mt_rand(1, 10);
$string = strval($randomNumber);
file_put_contents('../image/img.png', $imageData);
echo $imageData;
?>