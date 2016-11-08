var Class       = require('../core/class'),
    Component   = require('../core/component');

require('./menu.css');

var Menu = (function () {

    function Menu () {
        Component.call(this);
    }

    Class.inherit(Component, Menu);

    Menu.prototype.render = function () {
        this._$el.addClass('nav-menu');
        return this;
    };


    return Menu;

} ());

module.exports = Menu;
