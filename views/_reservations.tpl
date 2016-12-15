

<div id="reservations-div">
<!-- <div class="container"> -->
	<!-- <div class="row-fluid"> -->
	<!-- <div class="col-xs-12"> -->
		<div class="panel panel-default" id="reservations-panel">
			<div class="panel-heading">
				<h2 class="title">Reservations</h2>
			</div>
			<div class="panel-body">
			% for each in reservations:
				<div class="panel panel-default">
					<div class="panel-heading">
						<h3>{{each.name}}</h3>
					</div>

					% include('_data_pairs.tpl', data=each.data, filter=[])
				</div>
			% end
			</div>
		</div>
	<!-- </div>	 -->
	<!-- </div> -->
<!-- </div> -->
</div>