$(document).ready(function(){

    if (isMobile() === false){

	    $('#image-img img').load(function(){

		imgPosition = $('#image-img img').offset();
		
		$('#image-img p').css({
		    'position': 'absolute',
		    'left': imgPosition.left + 10,
		    'top': imgPosition.top - 10,
		});

	    });

	    $('#image-img img').hover(function(){

		imgPosition = $('#image-img img').offset();
		
		$('#image-img p').css({
		    'position': 'absolute',
		    'left': imgPosition.left + 10,
		    'top': imgPosition.top - 10,
		});

	    });
	}

});

function isMobile(){
    if ((navigator.userAgent.indexOf('iPhone') == -1) && (navigator.userAgent.indexOf('iPod') == -1) && (navigator.userAgent.indexOf('iPad') == -1)){
	return false;
    }
    return true;

}