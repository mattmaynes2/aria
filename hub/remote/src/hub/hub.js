var $           = require('jquery'),
    Class       = require('../core/class'),
    Widget      = require('./widget');

var Hub = (function () {

    function Hub () {
        Widget.call(this);
        this._state.title = 'Hub';
    }

    Class.inherit(Widget, Hub);

    Hub.prototype.render = function () {
        Widget.prototype.render.call(this);
        if (!this._$stateButton) {
            this._$stateButton = $('<button>').text('Refresh Status')
                .click(fetchStatus.bind(this));
            this._$el.find('.widget-footer').append(this._$stateButton);
        }

        return this;
    };

    function fetchStatus () {
        $.ajax({
            url     : '/request',
            type    : 'POST',
            data    : '{"action" : "status"}',
            headers : {
                'Content-Type' : 'application/json'
            }
        }).done((res) => {
            this._$el.find('.widget-body').empty().text(res);
        });
    }

    return Hub;
} ());

module.exports = Hub;
