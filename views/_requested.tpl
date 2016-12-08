<div class="container" id="requested-div">

	<div class="row">
		<div class="span12">

			<ul class="nav nav-tabs">
				<li class="active"><a href="#over-view" data-toggle="tab">Overview</a></li>
				<li><a href="#full-view" data-toggle="tab">Full view</a></li>
			</ul>
			
			<div class="tab-content">

				<div id="over-view" class="panel panel-default tab-pane fade in active">
					<div class="panel-heading">
						<h5>Scontrol output for <strong>node{{node.name}}</strong></h5>
					</div>

					<div class="panel-body">
						% overviewFields = ["NodeName", "CPUAlloc", "CPUErr", "CPUTot", "RealMemory", "AllocMem", "State"]
						% for key in sorted(node.data.keys()):
							% if key in overviewFields:
								<pre><span class="node-field-key">{{key}}</span> = <span class="node-field-val">{{node.data[key]}}</span></pre>
							% end
						% end
					</div>
				</div>

				<div id="full-view" class="panel panel-default tab-pane fade">
					<div class="panel-heading">
						<h5>Scontrol output for <strong>node{{node.name}}</strong></h5>
					</div>

					<div class="panel-body">
						% for key in sorted(node.data.keys()):
							<pre><span>{{key}}</span> = <span>{{node.data[key]}}</span></pre>
						% end
					</div>
				</div>

			</div>

		</div>
	</div>

</div>