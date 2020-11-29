function updatePercentage () {
    
    var elem = $(this);
    var current = elem.data("percent-current") || 0;
    
    var percent = parseFloat(current) + .1;
    var max = parseFloat(elem.data("percent"));
    if (percent > max) {
        percent = max;   
    }
    
    percent = percent.toFixed(1);
    
    deg = 360*percent/5;
    
    elem.data("percent-current", percent);
    
    elem.toggleClass('gt-50', percent > 2.5);
    
    elem.find('.ss-progress-fill').css('transform','rotate('+ deg +'deg)');	
    elem.find('.ss-percent span').html(percent);
    if (percent != max) {
        window.setTimeout( updatePercentage.bind(this), 100);        
    }
}

$(function(){
	var $ppc = $('.progress');
    $ppc.each(updatePercentage);    
});