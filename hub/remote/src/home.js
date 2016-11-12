import $            from 'jquery';
import Component    from './core/component';
import NavMenu      from './nav/menu';
import Hub          from './hub/hub';
import Device       from './hub/device';


class Home extends Component {

    constructor () {
        super();
        this._rendered = false;
        this._navmenu  = new NavMenu();
        this._hub      = new Hub();
        this._device   = new Device();
    }

    render () {
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


    }

}

export default Home;
