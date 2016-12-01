<div class="entry">

	<div class="row line">
		<a name="{{entryCounter}}" class="anchor"></a>
		<div class="col-md-2 node_name">
			<!-- % include('_nodenames.tpl', nodes=entry.nodes, entryIndex=entryCounter, requested=node) -->
			% include('_nodenames.tpl', nodes=entry.nodes)
		</div>
		<div class="col-md-3 node_time">
			<pre name="field">{{entry.time}}</pre>
		</div>
		<div class="col-md-7 node_reason">
			<pre name="field">{{entry.reason}}</pre>
		</div>
	</div>

	% if requestedLivesHere == entryCounter and not requestedInfoDisplayed:
		% requestedInfoDisplayed = True
		<div class="row" id="requested" data-anchor="{{entryCounter}}">
			<div class="col-md-12">

				<ul class="nav nav-tabs">
					<li class="over-view"><a href="#over-view" data-toggle="tab">Overview</a></li>
					<li class="full-view"><a href="#full-view" data-toggle="tab">Full view</a></li>
				</ul>
				
				<div class="tab-content">

					<div class="node-data" id="over-view" class="panel panel-default tab-pane fade in active">
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

					<div class="node-data" id="full-view" class="panel panel-default tab-pane fade">
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
	% end

	% if len(entry.nodes) > 1:
		<div class="row">
			<div class="col-md-12">
				<div class="nodelist" name="nodelist">
				% for n in entry.nodes:
					<a href="#" onclick="searchFromNodeList(this)" data-node="{{n}}">{{n}}</a>		
				% end
				</div>
			</div>
		</div>
	% end

</div>

