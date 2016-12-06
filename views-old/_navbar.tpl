<nav class="navbar navbar-default navbar-fixed-top">
	<div class="container-fluid">
		<div class="row">
			<div class="col-md-12">
				<ul class="nav nav-pills nav-list">
					% for s in sorted(states.keys()):
						<li class="nav-item">
							<a href="#{{s}}" class="btn btn-default nav-button">
								{{s}}
							</a>
						</li>
					% end
				</ul>
			</div>
		</div>

		<div class="row">
			<div class="col-md-12">
				% include('_search.tpl')
			</div>
		</div>
	</div>
</nav>