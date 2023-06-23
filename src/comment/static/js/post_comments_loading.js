$(document).ready(function() {
    $(".comment-button").click(function(e) {
        e.preventDefault();
        var post_id = $(this).data('post-id');
        var url = '/comment/ajax/comments/' + post_id + '/';
        $.ajax({
            url: url,
            type: 'get',
            dataType: 'json',
            success: function(data) {
                $('#comments-' + post_id).html(data.comments_html);
            }
        });
    });
});

