var $           = require('jquery'),
    Class       = require('../core/class'),
    Widget      = require('./widget');

var Device = (function () {

    function Device () {
        Widget.call(this);
        this._state.title = 'Device';
    }

    Class.inherit(Widget, Device);

    Device.prototype.render = function () {
        Widget.prototype.render.call(this);
        if (!this._$deviceButton) {
            this._$deviceButton = $('<button>').text('List Devices')
                .click(fetchDevices.bind(this));
            this._$el.find('.widget-footer').append(this._$deviceButton);
        }

        return this;
    };

    function fetchDevices () {
        $.ajax({
            url     : '/request',
            type    : 'POST',
            data    : '{"action" : "list_devices"}',
            headers : {
                'Content-Type' : 'application/json'
            }
        }).done((res) => {
            this._$el.find('.widget-body').empty().text(res);
        });
    }

    return Device;
} ());

module.exports = Device;
