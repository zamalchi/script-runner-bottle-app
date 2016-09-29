<!-- called from _outputs.tpl -->
<!-- nodelist : str -->

% from scripts.states_iterator import parseNodeList

<!-- a list to parse -->
% if '[' in nodelist:
	% parsed = parseNodeList(nodelist)
	<form action="/node" method="post" enctype="multipart/form-data">
		<select name="node" onclick="this.parentElement.submit()">
			% for node in parsed:
				<option name="nodeOption" value="{{node}}">
					node{{node}}
				</option>
			% end
		</select>
		<span>
			[{{len(parsed)}}]
		</span>
	</form>

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