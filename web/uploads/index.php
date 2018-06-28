<html><head></head><body>
<?php
$ip_address=$_SERVER['REMOTE_ADDR'];
$pw=$_GET["pass"];
$date=date('c');
#$date=date('l jS \of F Y h:i:s A');
$ip_string= $ip_address ." , ". $date;

// some code to be executed....
if ($pw=="secret"){
	$myfile = fopen("ip.txt", "w");
	fwrite($myfile,$ip_string);
	fclose($myfile);
	echo "<p>file written</p>";
}
else {
	$myfile = fopen("ip.txt", "r");
	$data=fgetcsv($myfile,1000,",");
	fclose($myfile);
	echo "<p>you are not the one I'm looking for</p>";
	echo "the IP of the other one is: $data[0] updated: $data[1]";
}

?>
<br><br><br><a href="showpic.php">show pic</a>
</body></html>