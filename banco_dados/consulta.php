<?php

header("Content-type: text/html; charset = utf-8");

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


$sql = "SELECT nome, salario FROM salario";


$result = mysqli_query($conn, $sql);

if (!$result) {
    echo "Não foi possível executar a consulta ($sql) no banco de dados: " . mysqli_error($conn);
    exit;
}

if (mysqli_num_rows($result) == 0) {
    echo "Não foram encontradas linhas, nada para mostrar";
    exit;
}

// Enquanto uma linha de dados existir, coloca esta linha em $row como uma matriz associativa
while ($row = mysqli_fetch_assoc($result)) {
    echo 'Nome: '.$row["nome"]."<br>";
    echo 'Salario: '.$row["salario"].'<br><br>';
}

mysqli_free_result($result);

?>
