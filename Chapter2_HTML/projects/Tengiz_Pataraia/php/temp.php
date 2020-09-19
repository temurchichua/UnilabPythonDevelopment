<?php
	
	require("database.php");

	$result = $db->query("SELECT * FROM user_registration_queue WHERE confirmation_key = 'bd0bd7c66aa14e843b07d4c168938de3'")->fetch();

	echo empty($result)?'true':'false';


?>