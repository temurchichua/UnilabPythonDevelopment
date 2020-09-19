<?php
session_start();
?>

<!DOCTYPE html>
<html>
<head>
	<title>Registration</title>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js"></script>
<link rel="stylesheet" type="text/css" href="../css/register.css">
</head>
<body>
	
	<div class="logo-container">
		<div class="row">
			<div class="col-lg-3 col-md-1"></div>
			<div class="col-lg-6 col-md-10">
				<center>
					<a href="../index.php"><img src="../img/logo.png" class="logo"></a>
				</center>
			</div>
			<div class="col-lg-3 col-md-1"></div>
		</div>
	</div>
	

	<div class="container">
		<div class="row">
			<div class="col-lg-3"></div>
			<div class="col-lg-6">
				<div id="ui">
					<div class="background">
					<form class="form-group" action="registration_handler.php" method="post">
						<div class="row">
							<div class="col-lg-6 col-md-6">
								<div class="label">First Name:</div>
								<input type="text" name="fname" class="form-control" placeholder="Enter your First name.." required>
							</div>
							
							<div class="col-lg-6 col-md-6">
								<div class="label">Last Name:</div>
								<input type="text" name="lname" class="form-control" placeholder="Enter your last name" required>
							</div>
						</div>
						<p style="color:red">
							<?php if(isset($_SESSION["errors"]["fname_error"])){
								echo $_SESSION["errors"]["fname_error"]."  ";
								}
								if(isset($_SESSION["errors"]["lname_error"])){
								echo $_SESSION["errors"]["lname_error"]."  ";
								}
							?>
						</p>

						<div class="row">
							<div class="col-lg-12">
								<div class="label">Nickname:</div>
								<input type="text" name="username" class="form-control" placeholder="Enter your Nickname" required>
							</div>
						</div>

						<p style="color:red">
							<?php if(isset($_SESSION["errors"]["username_error"])){
								echo $_SESSION["errors"]["username_error"]."  ";
								}
							?>
						</p>

						<div class="row">
							<div class="col-lg-12">
								<div class="label">E-mail</div>
		                        <input type="email" name="email" class="form-control" placeholder="Enter your E-mail..." required>
							</div>
						</div>

						<p style="color:red">
							<?php if(isset($_SESSION["errors"]["email_error"])){
								echo $_SESSION["errors"]["email_error"]."  ";
								}
							?>
						</p>
                        
						<div class="row">
							<div class="lebel">Your Data or Birth</div>
							<select name="month">
							<option value="month">Month</option>
							<option value="january">January</option>
							<option value="february">february</option>	
							</select>
							<select name="days">
								<option value="days">Days</option>
								<option value="1"> 1</option>
								<option value="2"> 2</option>
							</select>
							<select name="years">
								<option value="years">Years</option>
								<option value="1985">1985</option>
								<option value="1980">1980</option>
							</select>
						</div>
                        
                        <div class="row">
                        	<div class="col-lg-12">
	                        	<div class="label">Phone</div>
		                        <input type="text" name="phone" class="form-control" placeholder="Enter your phone number..." >
		                    </div>
                        </div>
                        
                        <div class="row">
							<div class="col-lg-6">
								<div class="label">Password:</div>
								<input type="password" name="password1" class="form-control" placeholder="Enter new password.." required>
							</div>
							
							<div class="col-lg-6">
								<div class="label">Re-type Password:</div>
								<input type="password" name="password2" class="form-control" placeholder="Re-type again.." required>
							</div>

						</div>

						<p style="color:red">
							<?php if(isset($_SESSION["errors"]["password_error"])){
								echo $_SESSION["errors"]["password_error"]."  ";
								}
								if(isset($_SESSION["errors"]["password_no_match"])){
								echo $_SESSION["errors"]["password_no_match"]."  ";
								}
							?>
						</p>

						<div class="label">Gender:</div>
						<select class="form-control">
							<option>Choose Gender..</option>
							<option>Male</option>
							<option>Female</option>
							<option>Others</option>
						</select>
						<br>
						<input type="submit" name="register" value="submmit" class="btn btn-primary btn-block btn-lg">
						
					</form>
					</div>
				</div>
			</div>
			<div class="col-lg-3"></div>

		</div>
	</div>
</body>
</html>

<?php
unset($_SESSION["errors"]);
?>