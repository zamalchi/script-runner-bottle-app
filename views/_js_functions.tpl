anchorHere(elem) {
	var anchor = elem.attributes["data-anchor"].value;
	window.location.hash = anchor;
}