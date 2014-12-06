$(function() {
	setInterval(function() {
		$.get('/get_time/', function(data) {
			$('#time').html(data);
		});
	}, 450);
})