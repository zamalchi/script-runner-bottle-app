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

						% lines = outputs[state]

						<div class="container" name="state-fields">
						% for l in lines:
							% if len(l.split("\t")) == 3:
								% nodelist, time, reasons = l.split("\t")
								<div class="row">
									<div class="col-md-3">
										<pre>{{nodelist}}</pre>
									</div>
									<div class="col-md-3">
										<pre>{{time}}</pre>
									</div>
									<div class="col-md-5">
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