<nav class="navbar navbar-default navbar-fixed-top">
<div class="container">

	<div class="navbar-brand">Slurm</div>
	<button class="navbar-toggle" data-toggle="collapse" data-target=".navHeaderCollapse">
		<span class="icon-bar"></span>
		<span class="icon-bar"></span>
		<span class="icon-bar"></span>
	</button>

	<div class="collapse navbar-collapse navHeaderCollapse">

		<ul class="nav navbar-nav navbar-right">
			% for s in sorted(states.keys()):
				<li><a href="#{{s}}">{{s}}</a></li>
			% end
		</ul>

	</div>

</div>
</nav>

<% '''
		% #####################################################################
		% # STATE NAV BUTTONS ROW
		<div class="row" id="state-nav-row">
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
	
		% # SEARCH BAR ROW
		<div class="row" id="search-bar-row">
			<div class="col-md-12">

				<form action="/node" method="post" enctype="multipart/form-data">

					<div class="form-group">
						<input type="hidden" id="search-anchor" name="anchor" value="">
						<%
						# id    : "search" : css
						# name  : "search" : bottle-form
						%>
						<input id="search" name="node" type="text"
								
								class="form-control input-lg"

								placeholder="node #"
								
								tabindex="1" accesskey="s" required>
					</div>

				</form>

			</div>
		</div>
		% #####################################################################

	</div>
</nav>
'''
%>