<!-- called from _outputs.tpl -->
<!-- nodelist : str -->

% from scripts.states_iterator import parseNodeList

<!-- a list to parse -->
% if '[' in nodelist:
	<select name="field">
		% for node in parseNodeList(nodelist):
			<option name="node" value="{{node}}">
				node{{node}}
			</option>
		% end
	</select>

<!-- a single node -->
% else:
	<a href="#">{{nodelist}}</a>
% end