<%
"""
This sub-template displays an individual entry as a part of a slurm state.
@:param entry: entry Python object.
@:param index: index of entry within the list of all entries from all states.
"""
%>
<div class="container-fluid entry">
	% ##################################################
	<div class="row data">
		% # * * * * * * * * * * * *	
		<a name="{{index}}" class="anchor"></a>
		% # * * * * * * * * * * * *
		<div class="col-md-2 nodes">
			% include('_nodes.tpl', nodes=entry.nodes, index=index)
		</div>
		% # * * * * * * * * * * * *
		<div class="col-md-3 time">
			<pre>{{entry.time}}</pre>
		</div>
		% # * * * * * * * * * * * *	
		<div class="col-md-7 reason">
			<pre>{{entry.reason}}</pre>
		</div>
		% # * * * * * * * * * * * *	
	</div>
	% ##################################################
	<%
	# LIST OF NODE-LINKS FOR QUICK SEARCH ON THE PAGE
	# DISPLAYS FOR ENTRIES WITH MORE THAN ONE NODE
	%>
	% if len(entry.nodes) > 1:
		<div class="row search-list">
		<div class="col-md-12">
			% for n in entry.nodes:
				<a href="#" onclick="searchFromNodeList(this)" data-node="{{n}}" data-anchor={{index}}>{{n}}</a>		
			% end
		</div>
		</div>
	% end
	% ##################################################
</div>
