loadSubPage('homepage.html');

function loadSubPage(url) {
	$("#page-wrapper").load(staticUrl + "subPages/" + url);
	// Morris Charts JavaScript
	$("body").append('<script src="' + staticUrl + 'vendor/raphael/raphael.min.js"></script>');
	$("body").append('<script src="' + staticUrl + 'vendor/morrisjs/morris.min.js"></script>');
	$("body").append('<script src="' + staticUrl + 'data/morris-data.js"></script>');
}

