<?php
    if (isset($_GET["submit"]))
    { 
      session_start();
      $_SESSION["txt"] = $_GET["txt"];
    } 
    $q1 = $_COOKIE["q1"];
    $q2 = $_COOKIE["esporte"];
    $q3 = $_COOKIE["animal"];
    $q4 = $_SESSION["eletrodomestico"];
    $q5 = $_SESSION["txt"];

    $total = 0;

    if ($q1 == "Laranja"){
        $total = 2;}
    if ($q2 == "Natação"){
      $total = $total + 2;}
    if ($q3 == "Polvo"){
      $total = $total + 2;}
    if ($q4 == "Geladeira"){
      $total = $total + 2;}
    if ($q5 == "Red" or $q5 == "red"){
      $total = $total + 2;}

?>
<html>
<meta charset="utf-8"/>
<head>
<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: center;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>
<h2 style="text-align:center">Página de Respostas</h2>
<body>
  <?php

    echo "<table>";
      echo "<tr>";
        echo "<th>Perguntas</th>";
        echo "<th>Respostas Corretas</th>";
        echo "<th>Suas Respostas</th>";
      echo "</tr>";
      echo "<tr>";
        echo "<td>Qual dessas é uma fruta cítrica?</td>";
        echo"<td>Laranja</td>";
        echo"<td>$q1</td>";
      echo "</tr>";
      echo "<tr>";
        echo "<td>Qual desses esportes NÃO utiliza bola?</td>";
        echo "<td>Natação</td>";
        echo "<td>$q2</td>";
      echo "</tr>";
      echo "<tr>";
        echo "<td>Qual desses é um animal aquático?</td>";
        echo "<td>Polvo</td>";
        echo "<td>$q3</td>";
      echo "</tr>";
      echo "<tr>";
        echo "<td>Selecione o eletrodoméstico?</td>";
        echo "<td>Geladeira</td>";
        echo "<td>$q4</td>";
      echo "</tr>";
      echo "<tr>";
        echo "<td>Como é vermelho em inglês?</td>";
        echo "<td>Red</td>";
        echo "<td>$q5</td>";
      echo "</tr>";
    echo "</table>";

    echo "<h2> Cada questão vale 2 pontos, totalizando 10 pontos."."<br></h2>";
    echo "<h2> Sua pontuação = " . $total. " pontos</h2>";
  ?>

</body>
  <button onclick="window.location.href = 'http://vivianne.great-site.net/quiz/q1.html'">Home</button>
<html>