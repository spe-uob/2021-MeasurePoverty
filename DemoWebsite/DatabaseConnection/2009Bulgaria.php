<?php
//$servername = "localhost";
$servername = "172.23.66.8";
$username = "root";
$password = "";
$dbname = "SPEtest";

// 创建连接
$conn = new mysqli($servername, $username, $password, $dbname);

// 检测连接
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
echo "Successfully Connected to the databases";


$sql = "SELECT questions FROM Bulgaria";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // 输出数据
    echo "<br>";
    echo "The data in the database is shown below:". "<br>". "<br>";
    while($row = $result->fetch_assoc()) {
        echo " " . $row["questions"]. "<br>";
    }
} else {
    echo "0 results";
}

$conn->close();//关闭连接
?>
