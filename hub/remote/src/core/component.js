var $ = require('jquery');

var Component = (function () {

    function Component () {
        this._state = {};
        this._$el = $('<div>');
    }

    Component.prototype.update = function (s) {
        this.state(s);
        return this;
    };

    Component.prototype.render = function () { return this; };


    Component.prototype.remove = function () {
        this._$el.remove();
        return this;
    };

    Component.prototype.$el = function (e) {
        if (arguments.length === 0) {
            return this._$el;
        }
        this._$el = e;
        return this;
    };

    Component.prototype.state = function (s) {
        if (arguments.length === 0) {
            return this._state;
        }
        this._state = s;
        return this;
    };

    return Component;
} ());

module.exports = Component;
