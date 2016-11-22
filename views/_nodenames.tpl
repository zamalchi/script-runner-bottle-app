<!-- called from _outputs.tpl -->
<!-- nodelist : str -->

<form action="/node" method="post" enctype="multipart/form-data">

<!-- for reloading the page to a specific location -->
<input type="hidden" name="anchor" value="{{anchor}}" />

<!-- a list to parse -->
% if len(nodes) > 1:

	<select name="node" onclick="this.parentElement.submit()">

		% for node in nodes:
			% if requested.name == node:
			<option name="nodeOption" value="{{node}}" selected>
			% else:
			<option name="nodeOption" value="{{node}}">
			% end
				node{{node}}
			</option>
		% end
	</select>

	<span class="label label-default" style="font-size: 1em;">
		{{len(nodes)}}
	</span>

<!-- a single node -->
% else:
	<input type="hidden" name="node" class="field" value="{{nodes[0]}}" />

	<button type="submit" class="button-center">
		node{{nodes[0]}}
	</button>

% end

</form>