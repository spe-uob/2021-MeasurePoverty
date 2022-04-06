<?php
//$servername = "localhost";
$servername = "127.0.0.19";
//makesure above is your localhost（if not,please change it）
$username = "root";
$password = "Change to your password！";
$dbname = "MesurePoverty";

// 创建连接
$conn = new mysqli($servername, $username, $password, $dbname);

// 检测连接
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
echo "Successfully Connected to the databases";


$sql = "SELECT * FROM Bulgaria2009";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // 输出数据
    echo "<br>";
    echo "The data in the database is shown below:". "<br>". "<br>";
    while($row = $result->fetch_assoc()) {
        echo " " . $row["questionNum"]." ".$row["pageNum"]." ".$row["questions"]." ".$row["uniID"]. "<br>";
    }
} else {
    echo "0 results";
}

$conn->close();//关闭连接
?>
