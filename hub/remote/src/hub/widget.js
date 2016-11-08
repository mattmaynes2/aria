var $           = require('jquery'),
    Class       = require('../core/class'),
    Component   = require('../core/component');

require('./widget.css');

var Widget = (function () {

    function Widget () {
        Component.call(this);
        this._state = {
            title   : 'Widget',
            body    : ''
        };
    }

    Class.inherit(Component, Widget);

    Widget.prototype.render = function () {
        if (this._$el.hasClass('widget-panel')) {
            return this;
        }


        this._$el
            .addClass('widget-panel')
            .append($('<div>').addClass('widget-header').text(this._state.title))
            .append($('<div>').addClass('widget-body').text(this._state.body))
            .append($('<div>').addClass('widget-footer'));

        return this;
    };

    return Widget;
} ());

module.exports = Widget;
