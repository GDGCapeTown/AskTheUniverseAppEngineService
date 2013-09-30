$(document).ready(function(){

	$(".questions li a").click(function(){

		$(this).parent().find('.answer-block').slideDown();

	});

});