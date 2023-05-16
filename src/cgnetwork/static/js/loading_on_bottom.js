$(window).scroll(function() {
  if($(window).scrollTop() + $(window).height() == $(document).height()) {
    $.get('jobs.html', {offset: currentOffset, limit: itemsPerPage}, function(data) {
      $('#pagination').append(data);
      currentOffset += itemsPerPage;
    });
  }
});
