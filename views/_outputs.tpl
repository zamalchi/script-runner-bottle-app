<div class="row-fluid" id="outputs">
	<div class="col-md-12">

	<hr />

	% # counter for entries (accumulated across all states)
	% entryCounter = 0

	% # ensures only one div is displayed when providing scontrol output (case : node in multiple states)
	% requestedInfoDisplayed = False 



	% for key in sorted(states.keys()):
		% state = states[key]
	
		% requestedLivesHere = state.findNodeInEntries(node.name)

		<div name="state" id="state-{{state.name}}">
			
			<div class="panel panel-default">

				<div class="panel-heading" style="padding: 0px;">
					<a name="{{state.name}}" class="anchor title-anchor"></a>
					<h2 name="state-title" style="margin: 0px 0px 10px 25px;">{{state.name}}</h2>
				</div>

				<div class="panel-body">


					<div class="container-fluid" name="state-fields">
				
					% for each in state.entries:
				
						<div class="entry">

							<div class="row line">
								<a name="{{entryCounter}}" class="anchor"></a>
								<div class="col-md-2 node_name">
									% include('_nodenames.tpl', nodes=each.nodes, entryIndex=entryCounter, requested=node)
								</div>
								<div class="col-md-3 node_time">
									<pre name="field">{{each.time}}</pre>
								</div>
								<div class="col-md-7 node_reason">
									<pre name="field">{{each.reason}}</pre>
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

											<div id="over-view" class="panel panel-default tab-pane fade in active" style="border: 1px solid grey;">
												<div class="panel-heading">
													<h5>Scontrol output for <strong>node{{node.name}}</strong></h5>
												</div>

												<div class="panel-body">
													% overviewFields = ["NodeName", "CPUAlloc", "CPUErr", "CPUTot", "RealMemory", "AllocMem", "State"]
													% for key in sorted(node.data.keys()):
														% if key in overviewFields:
															<pre style="display: inline-block; padding: 5px"><span style="color: blue">{{key}}</span> = <span style="color: green; font-weight: bold">{{node.data[key]}}</span></pre>
														% end
													% end
												</div>
											</div>

											<div id="full-view" class="panel panel-default tab-pane fade" style="border: 1px solid grey;">
												<div class="panel-heading">
													<h5>Scontrol output for <strong>node{{node.name}}</strong></h5>
												</div>

												<div class="panel-body">
													% for key in sorted(node.data.keys()):
														<pre style="display: inline-block; padding: 5px"><span style="color: blue">{{key}}</span> = <span style="color: green; font-weight: bold">{{node.data[key]}}</span></pre>
													% end
												</div>
											</div>

										</div>

									</div>
								</div>
							% end

							% if len(each.nodes) > 1:
								<div class="row">
									<div class="col-md-12">
										<div class="nodelist" name="nodelist">
										% for n in each.nodes:
											<a href="#" onclick="searchFromNodeList(this)" data-node="{{n}}">{{n}}</a>		
										% end
										</div>
									</div>
								</div>
							% end

							% i += 1
							% entry_counter += 1

						</div>

					% end

					</div>

				</div>
			
			</div>

			<hr />
		</div>

	% end
	
	</div>
</div>