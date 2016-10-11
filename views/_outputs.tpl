<div class="row" id="outputs">
	<div class="col-md-12">
	<hr />

	% for state in sorted(outputs.keys()):
		% if filter(None, outputs[state]):

			<div name="state" id="state-{{state}}">
				
				<div class="panel panel-default">

					<div class="panel-header">
						<h1 name="state-title">*** {{state}} ***</h1>
					</div>

					<div class="panel-body">

						% lines = outputs[state]

						<div class="container" name="state-fields">
						% for l in lines:
							% if len(l.split("\t")) == 3:
								% nodelist, time, reasons = l.split("\t")
								<div class="row">
									<div class="col-md-2">
										% include('__nodenames.tpl', nodelist=nodelist)
									</div>
									<div class="col-md-3">
										<pre name="field">{{time}}</pre>
									</div>
									<div class="col-md-6">
										<pre name="field">{{reasons}}</pre>
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