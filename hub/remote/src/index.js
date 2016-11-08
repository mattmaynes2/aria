var $       = require('jquery'),
    Home    = require('./home');

require('./index.css');

$(document).ready(() => {
    new Home().render();
});
