<!-- called from _outputs.tpl -->
<!-- nodelist : str -->

% from scripts.states_iterator import parseNodeList

<!-- a list to parse -->
% if '[' in nodelist:
	% parsed = parseNodeList(nodelist)
	<select name="field">
		% for node in parsed:
			<option name="node" value="{{node}}">
				node{{node}}
			</option>
		% end
	</select>
	<span>
		[{{len(parsed)}}]
	</span>

<!-- a single node -->
% else:
	% node = nodelist.replace('node', '')
	<form action="/node" method="post" enctype="multipart/form-data">
		<input type="hidden" name="node" value="{{node}}" />
		<button type="submit">
			{{nodelist}}
		</button>
	</form>
% end