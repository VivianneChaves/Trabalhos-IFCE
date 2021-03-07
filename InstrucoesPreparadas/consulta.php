<!-- ************ Consulta SQL com comandos preparados ******** -->

<html>
  <head>
        <title>CONSULTA BD</title>
        <meta charset="utf-8"/> 
        <style>
        table {
        font-family: arial, sans-serif;
        border-collapse: collapse;
        width: 70%;
        }

        td, th {
        border: 1px solid #dddddd;
        text-align: center;
        padding: 3px;
        }

        tr:nth-child(even) {
        background-color: #dddddd;
        }
        </style>
  </head>
    
<body> 
 
<?php
    
//Config. para acesso ao mySql localmente 
$servername = "sql311.epizy.com";
$username = "epiz_26899365";
$password = "EGacsonXcBn0v";
$dbname = "epiz_26899365_concurso";

$conn = mysqli_connect($servername, $username, $password);


if (!$conn) 
{
  die("Falha na Conexão: " . mysqli_connect_error());
}
echo "Conectado com Sucesso <BR><BR>";


// Selecionando banco
if (!mysqli_select_db($conn, $dbname)) 
{
    echo "Não foi possível selecionar base de dados \"$dbname\": " . mysqli_error($conn);
    exit;
}


$sql = "SELECT num_concurso, data_concurso, num_01, num_02, num_03 FROM concurso";

//stmt = statment ou comando
//stmt é o comando a ser preparado    
$stmt = mysqli_stmt_init($conn);    
$stmt_prepared_okay = mysqli_stmt_prepare($stmt, $sql);  
  
/* create a prepared statement */
if ($stmt_prepared_okay) 
{
    /* Liga parametros com os marcadores */
    //mysqli_stmt_bind_param($stmt, "i", $numc);

    /* executa a query */
    mysqli_stmt_execute($stmt);

    /* liga as variávais de resultado */
    mysqli_stmt_bind_result($stmt, $num_concurso, $data_concurso, $num_01, $num_02, $num_03);

    /* busca os valores */
    while(mysqli_stmt_fetch($stmt))
    {
          echo "<table>
    <tr>
      <th>Número do Bilhete</th>
      <th>Data de Emissão</th>
      <th>Número 1</th>
      <th>Número 2</th>
      <th>Número 3</th>
      <th>Excluir</th>
    </tr>
    <tr>
      <td> $num_concurso</td>
      <td> $data_concurso</td>
      <td> $num_01</td>
      <td> $num_02</td>
      <td> $num_03</td>
      <td> <a href=delete.php?num_concurso=$num_concurso> Deletar </a><br><br></td>
    </tr>
  </table>";
    }

    /* close statement */
    mysqli_stmt_close($stmt);
}    
    
?>

    <br><br>
    <button onclick="window.location.href ='q1.php'">Home</button>
</body>
</html> 