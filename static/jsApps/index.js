loadSubPage('homepage.html');

function loadSubPage(url) {
	$("#page-wrapper").load("/static/subPages/" + url);
	// Morris Charts JavaScript
	$("body").append('<script src="/static/vendor/raphael/raphael.min.js"></script>');
	$("body").append('<script src="/static/vendor/morrisjs/morris.min.js"></script>');
	$("body").append('<script src="/static/data/morris-data.js"></script>');
}

