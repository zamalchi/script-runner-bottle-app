<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" type="text/css" href="css/bootstrap.min.css"/>
 	<link rel="stylesheet" type="text/css" href="css/main.css" />

 	<link rel="shortcut icon" href="img/favicon.ico" />

 	<meta name="viewport" content="width=device-width, initial-scale=1.0">

	<!-- ######################################################################################################### -->
	<!-- SCRIPTS START -->	

 	<!-- jquery must come first and is required by bootstrap -->
	<script src="js/jquery-3.1.0.min.js"></script>
	<script src="js/bootstrap.min.js"></script>

	<!-- custom js functions -->
	% include('_js_functions.tpl')

	<!-- SCRIPTS END -->
	<!-- ######################################################################################################### -->

</head>


<!-- PASSED IN FROM ROUTE -->
<!-- time : current time -->
<!-- outputs : [str] from all the states -->

<body style="padding-top: 60px;">

<nav class="navbar navbar-default navbar-fixed-top" style="margin-top: 0px; padding: 10px; margin-bottom: 0px; background-color: lightgrey;">
	<div class="container-fluid">
		<ul class="nav nav-pills nav-justified">
			% for state in sorted(outputs.keys()):
				% if filter(None, outputs[state]):
					<li><a href="#{{state}}" style="font-size: 1.2em;" class="btn btn-default">{{state}}</a></li>
				% end
			% end
		</ul>
	</div>
</nav>

<!-- main container start -->
<div class="container" name="main">

<!-- outputs row start -->
% include('_outputs.tpl', anchorHere=anchor, requested=requested, scontrol_result=scontrol_result)
<!-- outputs row end -->

</div>
<!-- main container end -->

</body>

</html>