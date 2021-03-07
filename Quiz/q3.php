<?php
  $q2 = $_GET["esporte"];
  setcookie("esporte",$q2);
  
?>

<html>
  <head>
    <meta charset="utf-8"/>
  </head>
  <body>
    <form action="q4.php" method="get">
      <h2>3°) Qual desses é um animal aquático?</h2>
    
      <input type="radio" value="Leão" name="animal">Leão <br>
      <input type="radio" value="Gato" name="animal">Gato<br>
      <input type="radio" value="Polvo" name="animal">Polvo <br>
      <input type="radio" value="Elefante" name="animal">Elefante <br><br>
      
      <input type="submit" value="Enviar" name="submit_button"><br>

    </form>
  </body>
</html>
 



