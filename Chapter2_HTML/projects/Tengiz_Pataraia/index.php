<?php 
session_start();
?>

<!DOCTYPE html>
<html>
<head>
  <title>PokerMaster</title>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.8/css/solid.css">
  <script src="https://use.fontawesome.com/releases/v5.0.7/js/all.js"></script>
  <link rel="stylesheet" type="text/css" href="css/style.css">
</head>
<body>

<div class="logo-container">
	<div class="row">
		<div class="col-lg-6 col-md-10">
			<center>
				<a href="../index.php"><img src="../img/logo.png" class="logo"></a>
			</center>
		</div>
		<div class="col-lg-6 col-md-1"></div>
	</div>
</div>

<div class="container">
	<div class="model-dialog text-center">
	 		<div class="row">
		        <form class="col-12 col-xl-5 form-top" action="php/login.php" method="post">
		        	<div class="form-group">
		        		<input type="text" class="form-control" placeholder="Enter username" name="username">
		        		<?php if(isset($_SESSION["errors"]["username_error"])) : ?>
		    			<p style="color: red"> <?php echo($_SESSION["errors"]["username_error"]); ?> </p>
		    			<?php endif ?>
		        	</div>
		        	<div class="form-group">
		        		<input type="Password" class="form-control" placeholder="Enter password" name="password">
		        		<?php if(isset($_SESSION["errors"]["password_error"])) : ?>
		    			<p style="color: red"> <?php echo($_SESSION["errors"]["password_error"]); ?> </p>
		    			<?php endif ?>
		        	</div>

                    <div class="form-check">
                        <label class="form-check-label">
                           <input class="form-check-input" type="checkbox" name="remember"> Remember me
                        </label>
                    </div>
		        	<button type="submit" class="btn" name="login" ">Login</button>

		        </form>
	    	</div>
	    	<div class="row">
	    		<div class="col-12 col-xl-5 forgot form-bottom">
		        	<a href="php/Forgot Password.php">Forgot Password?</a><br>
		        	<?php if(isset($_SESSION["errors"]["wrongpass"])) : ?>
			    		<p style="color: red;"> <?php echo($_SESSION["errors"]["wrongpass"]); ?> </p>
			    	<?php endif ?>
		        	<a href="php/register.php">Sign up</a>
			    	<?php if(isset($_SESSION["errors"]["wrongpass"])) : ?>
			    		<p style="color: red;"> <?php echo($_SESSION["errors"]["wrongpass"]); ?> </p>
			    	<?php endif ?>
		    	</div>
	    	</div>
	        
	</div>
 </div> 

</body>
</html>

<?php
unset($_SESSION["errors"]);
?>
