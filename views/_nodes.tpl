<%
"""
@:param nodes: list of node numbers.
@:param index: index of entry within the list of all entries from all states.
"""
%>
<form action="/node" method="post" enctype="multipart/form-data">
% ##################################################
<input type="hidden" name="anchor" value="{{index}}" />
% ##################################################
% if len(nodes) > 1:
	<select name="node" onclick="this.parentElement.submit()">

		% for each in nodes:
			% if each.name == node.name:
			<option value="{{each}}" selected>
			% else
			<option value="{{each}}">
			% end
				node{{each}}
			</option>
		% end

	</select>

	<span class="label label-default node-count">
		{{len(nodes)}}
	</span>
% ##################################################
% else:
	<input type="hidden" name="node" value="{{nodes[0]}}" />

	<button type="submit" class="button-center">
		node{{nodes[0]}}
	</button>

% end
% ##################################################
</form>