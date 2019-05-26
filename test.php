<?php
$command = escapeshellcmd('./mealdeal.py');
$output = shell_exec($command);
echo $output;
?>
