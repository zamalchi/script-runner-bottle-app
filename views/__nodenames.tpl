<!-- called from _outputs.tpl -->
<!-- nodelist : str -->

% from scripts.states_iterator import parseNodeList

<form action="/node" method="post" enctype="multipart/form-data">

<!-- for reloading the page to a specific location -->
<input type="hidden" name="anchor" value="{{anchor}}" />

<!-- a list to parse -->
% if '[' in nodelist:
	% parsed = parseNodeList(nodelist)
	
	<select name="node" onclick="this.parentElement.submit()">

		% for node in parsed:
			% if str(requested) == str(node):
			<option name="nodeOption" value="{{node}}" selected>
			% else:
			<option name="nodeOption" value="{{node}}">
			% end
				node{{node}}
			</option>
		% end
	</select>

	<span class="label label-default" style="font-size: 1em;">
		{{len(parsed)}}
	</span>

<!-- a single node -->
% else:
	% node = nodelist.replace('node', '')

	<input type="hidden" name="node" class="field" value="{{node}}" />

	<button type="submit">
		{{nodelist}}
	</button>

% end

</form>