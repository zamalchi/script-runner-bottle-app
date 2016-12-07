<div class="container-fluid" name="states-container">
	<div class="row">
		<div class="col-md-12">
			<h3>States container!</h3>

			<%
				# counter for entries (accumulated across all states)
				entryCounter = 0

				# ensures only one div is displayed when providing scontrol output (case : node in multiple states)
				requestedInfoDisplayed = False 
			%>


			% for key in sorted(states.keys()):
				<%
				state = states[key]
				requestedLivesHere = state.findNodeInEntries(node.name) if not requestedInfoDisplayed else -1
				%>

				<!-- STATE START -->
				<div class="state" name="state" id="state-{{state.name}}">
					
					<div class="panel panel-default">

						<!-- PANEL-HEADING -->
						<div class="panel-heading">
							<!-- anchor for navbar navigation -->
							<a name="{{state.name}}" class="anchor title-anchor"></a>
							<!-- name of state -->
							<h2 class="state-title" name="state-title">{{state.name}}</h2>
						</div>

						<!-- PANEL-BODY -->
						<div class="panel-body">
							<!-- container of entry divs -->
							<div class="container-fluid" name="state-fields">
								% for each in state.entries:
									% entryCounter += 1
									% include("_entry.tpl", entry=each)
								% end 
							</div>
						</div>
					
					</div>

					<hr />
				</div>
				<!-- STATE END -->

			% end

		</div>
	</div>
</div>