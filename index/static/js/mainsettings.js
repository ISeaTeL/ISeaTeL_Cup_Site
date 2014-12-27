$(function() {
    $(document).tooltip({
        track: true
    });

    $('.ajax-form').submit(function() {
        form = $(this);

        $.ajax({
            type: $(this).attr('method'),
            url: $(this).attr('action'),
            data: $(this).serialize(),
            success: function(data) {
                form.html(data);
            },
            error: function(data) {
                $("#msg").html("Something went wrong!");
            }
        });
        return false;
    });
})
