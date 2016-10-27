<div class="row-fluid" id="outputs">
	<div class="col-md-12">

	<hr />

	% i = 0 # anchor counter index

	% for state in states:

		<div name="state" id="state-{{state}}">
			
			<div class="panel panel-default">

				<div class="panel-heading" style="padding-top: 0px;">
					<a name="{{state}}" class="anchor title-anchor"></a>
					<h2 name="state-title" style="margin-top: 0px;">{{state}}</h2>
				</div>

				<div class="panel-body">

					% sinfo_object = sinfo_output[state]
					% entries = sinfo_object.entries
					% requestedLivesHere = sinfo_object.findNodeInEntries(requested)

					<div class="container-fluid" name="state-fields">
				
					% entry_counter = 0 # entry counter

					% for each in entries:

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

						% if requestedLivesHere == entry_counter:
							<div class="row">
								<div class="col-md-12">
									<div class="panel panel-default" style="border: 1px solid grey;">
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
						% end

						% i += 1
						% entry_counter += 1

					% end

					</div>

				</div>
			
			</div>

			<hr />
		</div>

	% end
	
	</div>
</div>