<?php
if (isset($_GET["submit"]))
{
  session_start();
  $_SESSION["eletrodomestico"] = $_GET["eletrodomestico"];
}
?>

<!DOCTYPE html>
<html>
  <meta charset="utf-8"/>
  <body>

    
    <form action="q6.php" method="GET">
      <h2>5°) Como é "vermelho" em inglês?</h2>
      <input type="text" name="txt" >

      <input type="submit" value="Enviar" name="submit"><br>

    </form>

  </body>
</html>
