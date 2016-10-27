anchorHere() {
	var anchor = this.attributes["data-anchor"].value;
	window.location.hash = anchor;
}