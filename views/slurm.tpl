<%
''' Base template for the /slurm route
	:param anchor : ???
	:param states : dict(stateName: str --> objects: Slurm.State)
	:param node   : Slurm.Node object (use Node.found to check if exists)
'''
%>

<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" type="text/css" href="css/bootstrap.min.css"/>
 	<link rel="stylesheet" type="text/css" href="css/main.css" />

 	<link rel="shortcut icon" href="img/favicon.ico" />

 	<meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>


<!-- <body onload="anchorToRequested()"> -->
<body>

<!-- % include('_navbar.tpl', states=states) -->
% include('_navbar.tpl')

<!-- main container start -->
<div class="container-fluid" id="main-div">

	<div class="row-fluid">
		% ##################################################

		<div class="col-xs-4">
			% if node.found:
				% include('_requested.tpl')
			% end
		</div>
		
		% ##################################################
		
		<div class="col-xs-8 offset-xs-4">
			% include('_states.tpl')
		</div>
		
		% ##################################################
	</div>
</div>
<!-- main container end -->


<!-- ######################################################################################################### -->
<!-- SCRIPTS START -->	

	<!-- jquery must come first and is required by bootstrap -->
<script src="js/jquery-3.1.0.min.js"></script>
<script src="js/bootstrap.min.js"></script>

<!-- custom js functions -->
% include('_js_functions.tpl')

<!-- SCRIPTS END -->
<!-- ######################################################################################################### -->

</body>

</html>