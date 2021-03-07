<?php
$q3 = $_GET["animal"];
setcookie("animal",$q3);
?> 

<html>
  <meta charset="utf-8"/>
  <body>  

    <form action="q5.php" method="get">
      <h2>4°) Selecione o eletrodoméstico?</h2>
      
      <label for="eletrodomestico">Selecione o eletrodoméstico:</label>
      <select name="eletrodomestico">
        <option value="Sofá">Sofá</option>
        <option value="Cama">Cama</option>
        <option value="Geladeira">Geladeira</option>
        <option value="Estante">Estante</option>
      </select>
      
      <br><br><input type="submit" value="Enviar" name="submit"><br>

    </form>
  </body>
<html>


