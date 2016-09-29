<div class="row" id="outputs">
	<div class="col-md-12">
	<hr />

	% for state in sorted(outputs.keys()):
		% if filter(None, outputs[state]):

			<div name="state" id="state-{{state}}">
				
				<div class="panel panel-default">

					<div class="panel panel-header">
						<h4>*** {{state}} ***</h4>
					</div>

					<div class="panel panel-body">
						% if len(line.split("\t")) == 3:

							% lines = outputs[state]

							<div class="container">
							% for l in lines:
								% nodelist, time, reasons = line.split("\t")
								<div class="row">
									<div class="col-md-4">
										<pre>{{nodelist}}</pre>
									</div>
									<div class="col-md-4">
										<pre>{{time}}</pre>
									</div>
									<div class="col-md-4">
										<pre>{{reasons}}</pre>
									</div>
								</div>
								
							% end
						% end
						</div>

					</div>
				
				</div>

				<hr />
			</div>

		% end
	% end
	
	</div>
</div>