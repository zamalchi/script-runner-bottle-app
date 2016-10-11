<div class="row" id="outputs">
	<div class="col-md-12">
	<hr />

	% i = 0 # anchor counter index

	% for state in sorted(outputs.keys()):
		% if filter(None, outputs[state]):

			<div name="state" id="state-{{state}}">
				
				<div class="panel panel-default">

					<div class="panel-heading" style="padding-top: 0px;">
						<a name="{{state}}" class="anchor title-anchor"></a>
						<h2 name="state-title" style="margin-top: 0px;">{{state}}</h2>
					</div>

					<div class="panel-body">

						% lines = outputs[state]

						<div class="container-fluid" name="state-fields">

						% for l in lines:
							% if len(l.split("\t")) == 3:

								% nodelist, time, reasons = l.split("\t")
								<div class="row">
									<a name="{{i}}" class="anchor"></a>
									<div class="col-md-2">
										% include('__nodenames.tpl', nodelist=nodelist, anchor=i, requested=requested)
									</div>
									<div class="col-md-3">
										<pre name="field">{{time}}</pre>
									</div>
									<div class="col-md-6">
										<pre name="field">{{reasons}}</pre>
									</div>
								</div>

								% if str(anchorHere) == str(i):
									<div class="row">
										<div class="col-md-12">
											<div class="panel panel-default" style="border: 1px solid grey;">
												<div class="panel-heading">
													<h5>Scontrol output for <strong>node{{requested}}</strong></h5>
												</div>

												<div class="panel-body">
													% for line in scontrol_result.split("\n"):
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