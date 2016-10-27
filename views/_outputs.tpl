<div class="row-fluid" id="outputs">
	<div class="col-md-12">

	<hr />

	% i = 0 # anchor counter index
	% requestedInfoDisplayed = False # ensures only one div is displayed when providing scontrol output (case : node in multiple states)

	% for state in states:

		<div name="state" id="state-{{state}}">
			
			<div class="panel panel-default">

				<div class="panel-heading" style="padding: 0px;">
					<a name="{{state}}" class="anchor title-anchor"></a>
					<h2 name="state-title" style="margin: 0px 0px 10px 25px;">{{state}}</h2>
				</div>

				<div class="panel-body">

					% sinfo_object = sinfo_output[state]
					% entries = sinfo_object.entries
					% requestedLivesHere = sinfo_object.findNodeInEntries(requested)

					<div class="container-fluid" name="state-fields">
				
					% entry_counter = 0 # entry counter

					% for each in entries:

						<div class="entry">

							<div class="row line">
								<a name="{{i}}" class="anchor"></a>
								<div class="col-md-2 node_name">
									% include('_nodenames.tpl', nodes=each.nodes, anchor=i, requested=requested)
								</div>
								<div class="col-md-3 node_time">
									<pre name="field">{{each.time}}</pre>
								</div>
								<div class="col-md-7 node_reason">
									<pre name="field">{{each.reason}}</pre>
								</div>
							</div>

							% if requestedLivesHere == entry_counter and not requestedInfoDisplayed:
								% requestedInfoDisplayed = True
								<div class="row" id="requested" data-anchor="{{i}}">
									<div class="col-md-12">
			
										<ul class="nav nav-tabs">
											<li class="over-view"><a href="#over-view" data-toggle="tab">Overview</a></li>
											<li class="full-view"><a href="#full-view" data-toggle="tab">Full view</a></li>
										</ul>
										
										<div class="tab-content">

											<div id="over-view" class="panel panel-default tab-pane fade in active" style="border: 1px solid grey;">
												<div class="panel-heading">
													<h5>Scontrol output for <strong>node{{requested}}</strong></h5>
												</div>

												<div class="panel-body">
													% overviewFields = ["NodeName", "CPUAlloc", "CPUErr", "CPUTot", "RealMemory", "AllocMem", "State"]
													% for line in scontrol_output.split("\n"):
														% for field in line.split(" "):
															% if '=' in field:
																% key, val = field.split("=")
																% if key in overviewFields:
																	<pre style="display: inline-block; padding: 5px"><span style="color: blue">{{key}}</span> = <span style="color: green; font-weight: bold">{{val}}</span></pre>
																% end
															% end
														% end
													% end
												</div>
											</div>

											<div id="full-view" class="panel panel-default tab-pane fade" style="border: 1px solid grey;">
												<div class="panel-heading">
													<h5>Scontrol output for <strong>node{{requested}}</strong></h5>
												</div>

												<div class="panel-body">
													% for line in scontrol_output.split("\n"):
														% for field in line.split(" "):
															% if '=' in field:
																% key, val = field.split("=")
																<pre style="display: inline-block; padding: 5px"><span style="color: blue">{{key}}</span> = <span style="color: green; font-weight: bold">{{val}}</span></pre>
															% end
														% end
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
										<textarea class="nodelist" rows="2" readonly name="nodelist">
										% for node in each.nodes:
											<a href="#" onclick="searchFromNodeList(this)" data-node="{{node}}">{{node}}</a>		
										% end
										</textarea>
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