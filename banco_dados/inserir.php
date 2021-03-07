<?php

header("Content-type: text/html; charset = utf-8");
//mysqli_set_charset('UTF-8');

//Config. para acesso ao mySql no infinityfree
/*$servername = "";
$username = "";
$password = "";
$dbname = "";*/

//Config. para acesso ao mySql localmente
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "tabela";

$conn = mysqli_connect($servername,$username,$password);

if (!$conn) {
    echo "Não foi possível conectar ao banco de dados: " . mysqli_connect_error();
    exit;
}


// Selecionando banco
if (!mysqli_select_db($conn,$dbname)) {
    echo "Não foi possível selecionar o banco de dados \"$dbname\": " . mysqli_error($conn);
    exit;
}



$sql = "INSERT INTO salario (nome, salario) VALUES
		('RAIMUNDO', 600.0),
		('LOPES', 600.0),
		('SOUZA', 2640.60),
		('FRANCISCO', 600.0)";



$result = mysqli_query($conn, $sql);

if ($result) {
	echo "Os registros foram inseridos com sucesso.";
} else {
    echo "Não foi possível executar ($sql) no banco de dados: $dbname" . mysqli_error($conn);
    exit;
}

mysqli_free_result($result);

?>
