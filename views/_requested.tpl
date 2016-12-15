<%
"""
This sub-template displays scontrol information for a requested node.
"""
overviewFields = ["NodeName", "CPUAlloc", "CPUErr", "CPUTot", "RealMemory", "AllocMem", "State"]
%>

<div id="requested-div">

<div class="row-fluid">
<!-- <div class="col-xs-12"> -->

	% ##################################################
	<ul class="nav nav-tabs">
		<li class="active">
			<a href="#over-view" data-toggle="tab">Overview</a>
		</li>
		<li>
			<a href="#full-view" data-toggle="tab">Full view</a>
		</li>
	</ul>
	% ##################################################
	<div class="tab-content">
		% # * * * * * * * * * * * *
		<div id="over-view" class="panel panel-default tab-pane fade in active">
			<div class="panel-heading">
				<h5>Scontrol output for <strong>node{{node.name}}</strong> in <strong>{{node.data.get("State")}}</strong></h5>
			</div>
			% include('_data_pairs.tpl', data=node.data, filter=overviewFields)
		</div>
		% # * * * * * * * * * * * *
		<div id="full-view" class="panel panel-default tab-pane fade">
			<div class="panel-heading">
				<h5>Scontrol output for <strong>node{{node.name}}</strong> in <strong>{{node.data.get("State")}}</strong></h5>
			</div>
			% include('_data_pairs.tpl', data=node.data, filter=[])
		</div>
		% # * * * * * * * * * * * *
	</div>
	% ##################################################

<!-- </div> -->
</div>

</div>