var $ = require('jquery');

$(document).ready(() => {
    $('body').append(
        $('<button>').text('Status').click(() => {
            $.ajax('/system/state').done((res) => {
                $('body').append(res);
            });
        })
    );
});
