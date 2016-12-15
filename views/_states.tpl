<%
"""
This sub-template displays sinfo information about the different slurm states.
"""

# counter for entries (accumulated across all states)
entryCounter = 0
%>

<div class="container-fluid" id="states-div">
<div class="row-fluid">
<!-- <div class="col-xs-12"> -->

	% for key in sorted(states.keys()):
		% state = states.get(key)
		% ##################################################
		<div class="state" id="state-{{state.name}}">
			
			<div class="panel panel-default">
				% # * * * * * * * * * * * *
				<div class="panel-heading">
					<!-- anchor for navbar navigation -->
					<a name="{{state.name}}" class="anchor"></a>
					<!-- name of state -->
					<h2 class="title">{{state.name}}</h2>
				</div>
				% # * * * * * * * * * * * *	
				<div class="panel-body">
					% for each in state.entries:
						% include("_entry.tpl", entry=each, index=entryCounter)
						% entryCounter += 1
					% end
				</div>
				% # * * * * * * * * * * * *
			</div>
			
			<hr />
		</div>
		% ##################################################
	% end

<!-- </div> -->
</div>
</div>