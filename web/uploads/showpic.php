<html><head></head><body><p></p>
<?php
$filename="files/bild.jpg";
echo "<p>last upload:";
echo date("d F Y H:i:s.",filemtime($filename));
echo "</p>";
?>
<img src="<?php echo $filename; ?>" width="100%">
</body></html>