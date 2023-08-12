/* fixed-header*/
$(function() {
    var header = $("#header"),
    introH = $("#intro").innerHeight(),
    scrollOffset = 0; 

    $(window).on('scroll', function() {

        scrollOffset = $(this).scrollTop();

        if (scrollOffset >= introH + 500) {
            header.addClass('fixed');
        } else {
            header.removeClass('fixed');
        }

        
    })
});

/*smooth scroll*/

$("[data-scroll]").on('click', function(event) {

    event.preventDefault();
    
    var $this = $(this),
    block = $this.data('scroll'),
    blockOffset = $(block).offset().top;
    
    $('#nav a').removeClass('active');
    $this.addClass('active');

    $('html, body').animate({
        scrollTop: blockOffset
    });
});



/* nav toggle */

$('#nav_toggle').on('click', function(event){
    event.preventDefault()


    $(this).toggleClass('active'); 
    $('#nav').toggleClass('active');
    $('#header').toggleClass('active');
   
});



