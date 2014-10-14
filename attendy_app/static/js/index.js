$(document).ready(function() {

    $.ajax({
        url: '/get_mayor',
        type: "GET",
        success: function(data) {
            console.log(data);
            $('#mayor').append("<p>Todays mayor is " + data[0].fields.username + "</p>");
        }
    })
});

