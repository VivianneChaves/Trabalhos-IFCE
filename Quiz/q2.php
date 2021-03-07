<?php
  $q1 = $_GET['q1'];
  setcookie("q1",$q1);
?>

<!DOCTYPE HTML>  
<html>
  <head>
    <meta charset="utf-8"/>
  </head>
    <body>  
      <form action="q3.php" method="get">
        <h2>2°) Qual desses esportes NÃO utiliza bola?</h2>
        
        <input type="checkbox" value="Futebol" name="esporte">Futebol <br>
        <input type="checkbox" value="Natação" name="esporte">Natação <br>
        <input type="checkbox" value="Volêi" name="esporte">Volêi <br>
        <input type="checkbox" value="Ping Pong" name="esporte">Ping Pong <br><br>
        
        <input type="submit" value="Enviar" name="submit_button"><br>

      </form>
    </body>
</html>

