var Class       = require('../core/class'),
    Component   = require('../core/component');

var Hub = (function () {

    function Hub () {
        Component.call(this);
    }

    Class.inhert(Component, Hub);

    Hub.prototype.render = function () {
    };



    return Hub;
} ());

module.exports = Hub;
