<div class="entry">
	<%
	# NODES, TIME, REASON
	# ALWAYS DISPLAYS
	%>
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

	% ##################################################################################

	<%
	# DATA FROM `SCONTROL SHOW NODE`
	# DISPLAYS ONLY IF A NODE HAS BEEN REQUESTED AND IT LIVES IN THIS ENTRY -->
	%>
	% if requestedLivesHere == entryCounter and not requestedInfoDisplayed:
		% requestedInfoDisplayed = True
		% include("_requested.tpl")
	% end

	% ##################################################################################

	<%
	# LIST OF NODE-LINKS FOR QUICK SEARCH ON THE PAGE
	# ALWAYS DISPLAYS FOR ENTRIES WITH MORE THAN ONE NODE
	%>
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

