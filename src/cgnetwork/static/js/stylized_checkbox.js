$(document).ready(function() {
    $('input[type=checkbox]').each(function() {
        $(this).wrap('<label class="switch"></label>').after('<span class="slider round"></span>');
    });
});
