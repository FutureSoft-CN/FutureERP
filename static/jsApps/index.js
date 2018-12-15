loadSubPage('dashboard.html');

function loadSubPage(url) {
	$("#page-wrapper").load(staticUrl + "subPages/" + url);
}

