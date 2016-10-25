<nav class="navbar navbar-default navbar-fixed-top">
	<div class="container-fluid">
		<ul class="nav nav-pills nav-list">
			% for state in states:
				<li class="nav-item">
					<a href="#{{state}}" class="btn btn-default nav-button">
						{{state}}
					</a>
				</li>
			% end
		</ul>
	</div>
</nav>