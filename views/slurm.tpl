<%
''' Base template for the /slurm route
	:param anchor : ???
	:param states : dict(stateName: str --> objects: Slurm.State)
	:param node   : Slurm.Node object (use Node.found to check if exists)
'''
%>
% ########################################
<!DOCTYPE html>
<html>
% ########################################
<head>
	<link rel="stylesheet" type="text/css" href="css/bootstrap.min.css"/>
 	<link rel="stylesheet" type="text/css" href="css/main.css" />

 	<link rel="shortcut icon" href="img/favicon.ico" />

 	<meta name="viewport" content="width=device-width, initial-scale=1.0">

 	<title>Slurm</title>
</head>
% ########################################

% ########################################
<body>
<!-- CONTAINER -->
<div class="container">

<!-- HEADER -->
<div class="header">
	% include('_navbar.tpl')
</div>

<!-- CONTENT AREA -->
<div id="content_area">
	<div id="left_col">Left col</div>
	<div id="right_col">Right col</div>
</div>

<!-- FOOTER -->
<div class="footer">Footer</div>

</div> <!-- END OF CONTAINER -->

% ########################################

<!-- jquery must come first and is required by bootstrap -->
<script src="js/jquery-3.1.0.min.js"></script>
<script src="js/bootstrap.min.js"></script>

<!-- custom js functions -->
% include('_js_functions.tpl')

% ########################################
</body>
% ########################################
</html>
% ########################################


<% '''
<!-- main container start -->
<div class="container-fluid" id="main-div">

	<div class="row-fluid">
		% ##################################################

		<div class="col-xs-6">
		<div class="container-fluid" id="left-subdiv">
			<div class="row-fluid">
			<!-- <div class="col-xs-12"> -->
			% if node and node.found:
				% include('_requested.tpl')
			% end
			<!-- </div> -->
			</div>
			
			<div class="row-fluid">
			<!-- <div class="col-xs-12"> -->
			% if reservations:
				% include('_reservations.tpl')
			% end
			<!-- </div> -->
			</div>
		</div>
		</div>
		
		% ##################################################
		
		<div class="col-xs-6 offset-xs-6">
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
</div>

</body>

</html>
'''%>
