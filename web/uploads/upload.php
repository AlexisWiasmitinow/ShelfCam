<?php
#phpinfo();
$uploads_dir = './files';
#$destination = $uploads_dir."/".$_FILES["upfile"]["name"];
$destination = $uploads_dir."/bild.jpg";
#print_r($_FILES["upfile"]["tmp_name"]);
print_r($_FILES);
print("\n uploaded $destination");
move_uploaded_file($_FILES["upfile"]["tmp_name"],$destination);
/*
foreach ($_FILES["pictures"]["error"] as $key => $error) {
    if ($error == UPLOAD_ERR_OK) {
        $tmp_name = $_FILES["pictures"]["tmp_name"][$key];
        // basename() may prevent filesystem traversal attacks;
        // further validation/sanitation of the filename may be appropriate
        $name = basename($_FILES["pictures"]["name"][$key]);
        move_uploaded_file($tmp_name, "$uploads_dir/$name");
        echo "<p>uploaded</p>";
    }
    else {
    	echo "<p>something went wrong</p>";
    }
}
*/
?>