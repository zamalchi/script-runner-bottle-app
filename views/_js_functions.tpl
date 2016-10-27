<script type="text/javascript">


function anchorToRequested () {
	var requested = document.getElementById("requested");
	var anchor = requested.attributes["data-anchor"].value;
	window.location.hash = anchor;
}

function searchFromNodeList(elem) {
	var search = document.getElementById("search");
	var node = elem.attributes["data-node"].value;

	search.value = node;
	search.form.submit();
}

</script>