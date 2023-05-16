$(document).ready(function() {
  $('#sticky-menu a').click(function(event) {
    event.preventDefault();
    var href = $(this).attr('href');
    $('html, body').animate({
      scrollTop: $(href).offset().top
    }, 500);
  });
});