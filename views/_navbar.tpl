<nav class="navbar navbar-default navbar-fixed-top">
	<div class="container-fluid">
		<ul class="nav nav-pills nav-list">
			% for state in sorted(outputs.keys()):
				% if filter(None, outputs[state]):
					<li class="nav-item">
						<a href="#{{state}}" class="btn btn-default nav-button">
							{{state}}
						</a>
					</li>
				% end
			% end
		</ul>
	</div>
</nav>