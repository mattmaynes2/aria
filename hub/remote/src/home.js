var $           = require('jquery'),
    Class       = require('./core/class'),
    Component   = require('./core/component'),
    NavMenu     = require('./nav/menu'),
    Hub         = require('./hub/hub'),
    Device      = require('./hub/device');

var Home = (function () {

    function Home () {
        Component.call(this);
        this._rendered = false;
        this._navmenu = new NavMenu();
        this._hub = new Hub();
        this._device = new Device();
    }

    Class.inherit(Component, Home);

    Home.prototype.render = function () {
        $('body')
            .append(this._navmenu.$el())
            .append(this._hub.$el())
            .append(this._device.$el());

        this._navmenu.render();

        // TODO Remove inline CSS
        this._hub.render().$el().css({
            top         : '50px',
            position    : 'absolute'
        });

        // TODO Remove inline CSS
        this._device.render().$el().css({
            top         : '150px',
            position    : 'absolute'
        });


    };


    return Home;
} ());

module.exports = Home;

