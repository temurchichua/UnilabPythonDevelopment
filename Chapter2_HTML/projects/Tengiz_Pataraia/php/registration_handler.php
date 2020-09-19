<?php

session_start();

require 'PHPMailer/src/Exception.php';
require 'PHPMailer/src/PHPMailer.php';
require 'PHPMailer/src/SMTP.php';

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\SMTP;
use PHPMailer\PHPMailer\Exception;

require("database.php");

$checkKey 		= $db->prepare("SELECT * FROM user_registration_queue WHERE confirmation_key = ?");
$putInQueue		= $db->prepare("INSERT INTO user_registration_queue (firstname,lastname,username,password,birth_date,phone,email,confirmation_key) VALUES (?, ?, ?, ?, ?, ?, ?, ?)");
$checkUsername	= $db->prepare('SELECT id FROM users WHERE username = ? UNION SELECT id FROM user_registration_queue WHERE username = ?');
$checkEmail		= $db->prepare("SELECT email FROM users WHERE email = ? UNION SELECT email FROM user_registration_queue WHERE email = ?");


$mail = new PHPMailer(true);

//Server settingsdebug output
//$mail->SMTPDebug = SMTP::DEBUG_SERVER; 
$mail->isSMTP();                                            // Send using SMTP
$mail->Host       = 'smtp.elasticemail.com';                    // Set the SMTP server to send through
$mail->SMTPAuth   = true;                                   // Enable SMTP authentication
$mail->Username   = 'pokermaster.ge@elasticemail.com';                     // SMTP username
$mail->Password   = 'DDB9D2FF8705AFFF35B388BF170728305109';                               // SMTP password
$mail->SMTPSecure = "tls";
$mail->Port       = 2525;                                    // TCP port to connect to, use 465 for `PHPMailer::ENCRYPTION_SMTPS` above

//Recipients
$mail->setFrom('pokermaster.ge@gmail.com', 'pokermaster.ge');


if($_SERVER["REQUEST_METHOD"] == "POST"){
	if(isset($_POST["register"])){
		$errors = array();
		if(empty($_POST["username"])){
			$errors = array_merge($errors,["username_error" => "Nickname not defined"]);
		}else{
			$username = $_POST["username"];
		}
		if(empty($_POST["fname"])){
			$errors = array_merge($errors,["fname_error" => "First name not defined"]);
		}else{
			$fname = $_POST["fname"];
		}
		if(empty($_POST["lname"])){
			$errors = array_merge($errors,["lname_error" => "Last name not defined"]);
		}else{
			$lname = $_POST["lname"];
		}
		if(empty($_POST["email"])){
			$errors = array_merge($errors,["email_error" => "Email not defined"]);
		}else{
			$email = $_POST["email"];
		}
		
		$phone = null;
//		if(empty($_POST["phone"])){
//			$errors = array_merge($errors,["phone_error" => "Phone number not defined"]);
//		}else{
//			$phone = $_POST["phone"];
//		}
		if(empty($_POST["password1"])){
			$errors = array_merge($errors,["password_error" => "Password not defined"]);
		}else{
			$password1 = $_POST["password1"];
		}
		if(empty($_POST["password2"])){
			$errors = array_merge($errors,["password_error" => "Password not defined"]);
		}else{
			$password2 = $_POST["password2"];
		}
		if($password1 !== $password2){
			$errors = array_merge($errors,["password_no_match" => "Passwords don't match"]);
		}else{
			$password = md5($password1);
		}

		if(empty($errors)){
			$checkUsername->execute([$username,$username]);
			if(!empty($checkUsername->fetch())){
				$errors = array_merge($errors,["username_error" => "Nickname already occupied"]);
			}else{
				$checkEmail->execute([$email,$email]);
				if(!empty($checkEmail->fetch())){
					$errors = array_merge($errors,["email_error" => "Email already used"]);
				}else{

					$key = md5(rand());
					$checkKey->execute([$key]);

					while(!empty($checkKey->fetch())){
						$key = md5(rand());
						$checkKey->execute([$key]);
					}

					try{
						$mail->addAddress($email);        
						$mail->isHTML(true); 
						$mail->Subject = 'Confirm email';
						$mail->Body    = "<a href='http://pokermaster.000webhostapp.com/confirm.php?key=$key'>Click here to confirm email</a>";

						$mail->send();
						echo 'Message has been sent';
						$putInQueue->execute([$fname,$lname,$username,$password,"2000-01-01",$phone,$email,$key]);
					} catch (Exception $e) {
					    echo "Message could not be sent. Mailer Error: {$mail->ErrorInfo}";
					}

				}
			}


		}
		if(!empty($errors)){
			$_SESSION["errors"] = $errors;
			header("location:register.php");
		}

	}
}



?>