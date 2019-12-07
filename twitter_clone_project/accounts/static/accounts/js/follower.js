$(".follower").click(function () {
    var button_value = $(this).text();
    var username = $(this).parent().parent().find('a')[0]
    var thisObject = this

    $.ajax({
        url: '../ajax/change-follow-status',
        method: "GET",
        data: {
            "status": button_value,
            "username": username.text
        },
        dataType: 'json',
        success: function (data) {
            $(thisObject).html(data.status)
        }
    })
});

$(".follower").each(function () {
    var button_value = $(this).text();
    var username = $(this).parent().parent().find('a')[0]
    var thisObject = this

    $.ajax({
        url: '../ajax/check-follow-status',
        method: "GET",
        data: {
            "status": button_value,
            "username": username.text
        },
        dataType: 'json',
        success: function (data) {
            $(thisObject).html(data.status)
        }
    })
});