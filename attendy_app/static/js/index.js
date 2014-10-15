$(document).ready(function() {

    $.ajax({
        url: '/get_mayor',
        type: "GET",
        success: function(data) {
            console.log(data);
            $('#mayor').append("<p>Todays mayor is " + data[0].fields.username + "</p>");
        }
    });


$("#check_in").on('click', function() {
        checkIn();
    });

    var checkIn = function () {
        $.ajax({
            url: '/check_in',
            type: "GET",
            success: function (data) {
                $('#checked_in').append("<p>Hello " + data[0].fields.username + ", you sucessfully checked in! </p>" +
                    "<p>You have checked in " + data[0].fields.check_in_counter +" times, since you have registered! </p> ")
                console.log(data);
            }
        })
    }

    });

