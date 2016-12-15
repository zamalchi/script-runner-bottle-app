
<div class="panel-body data-pairs">
	% for key in sorted(data.keys()):
		% if (filter and key in filter) or not filter:
			<pre><span class="node-field-key">{{key}}</span> = <span class="node-field-val">{{data.get(key)}}</span></pre>
		% end
	% end
</div>