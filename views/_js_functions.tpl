<script type="text/javascript">


function anchorToRequested () {
	var requested = document.getElementById("requested");
	var anchor = requested.attributes["data-anchor"].value;
	window.location.hash = anchor;
}

function searchFromNodeList(elem) {
	var search = document.getElementById("search");
	var anchor = document.getElementById("search-anchor")

	var node = elem.attributes["data-node"].value;
	var index = elem.attributes["data-anchor"].value;

	search.value = node;
	anchor.value = index;

	search.form.submit();
}

</script>