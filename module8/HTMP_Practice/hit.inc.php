<?php
  $countFile = "hit.txt";
  $hits = file($countFile);
  $hits[0] ++;

  //$fp = fopen($countFile , "w");
  if (!$fp = fopen($countFile, 'w')) {
         echo "Не могу открыть файл $countFile";
         exit;
    }
  fputs($fp, $hits[0]);
  fclose($fp);

?>
