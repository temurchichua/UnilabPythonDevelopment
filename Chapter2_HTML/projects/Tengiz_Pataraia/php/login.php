<?php

session_start();

require("database.php");

$checkuser = $db->prepare("SELECT * FROM users WHERE username=? AND password=?");

if($_SERVER["REQUEST_METHOD"] == "POST"){
	$username = "";
	$password = "";
	$errors = array();

	if(empty($_POST["username"])){
		$errors = array_merge($errors,["username_error" => "Username field is empty"]);
	}else{
		$username = $_POST["username"];
	}
	if(empty($_POST["password"])){
		$errors = array_merge($errors,["password_error" => "Password field is empty"]);
	}else{
		$password = md5($_POST["password"]);
	}
	if(count($errors) > 0){
		$_SESSION["errors"] = $errors;
		header("location:../index.php");
	}

	$checkuser->execute([$username,$password]);
	$result = $checkuser->fetch();

	if(!empty($result)){
		$_SESSION["username"] = $username;
		$_SESSION["auth_success"] = "Succesfully logged in";
		header("location:game.php");
	}else{
		$errors = array_merge($errors,["wrongpass" => "Wrong username or password"]);
		$_SESSION["errors"] = $errors;
		header("location:../index.php");
	}

}else{
	$_SESSION["errors"] = NULL;
}

$db = NULL;

?>