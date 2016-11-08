var $           = require('jquery'),
    Class       = require('./core/class'),
    Component   = require('./core/component'),
    NavMenu     = require('./nav/menu');

var Home = (function () {

    function Home () {
        Component.call(this);
        this._rendered = false;
        this._navmenu = new NavMenu();
    }

    Class.inherit(Component, Home);

    Home.prototype.render = function () {
        $('body').append(this._navmenu.$el());
        this._navmenu.render();

    };


    return Home;
} ());

module.exports = Home;

