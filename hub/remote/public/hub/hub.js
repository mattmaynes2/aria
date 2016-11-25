import $            from 'jquery';
import Widget       from '../core/widget/widget';
import Button       from '../core/control/button';
import StateButton  from '../core/control/state-button';
import Service      from '../core/service/service';
import Notify       from '../core/notify/notify';
import './hub.css';

class Hub extends Widget {
    static get modes () {
        return ['Standby', 'Normal', 'Learning'];
    }

    static mode (m) {
        return typeof m === 'string' ?
            Hub.modes.indexOf(m) :
            Hub.modes[m];
    }

    constructor () {
        super();
        this._state = {
            title   : 'Smart Hub',
            version : '',
            mode    : 0,
            devices : 0
        };
        this._stateButton = new StateButton(Hub.modes);
        this._stateButton.change((button) => {
            Service.set('/hub/mode', { mode : Hub.mode(button.val()) })
                .then((res) => {
                    this._state.mode = res.mode;
                    this.render();
                });
        });
        this._discoverButton = new Button('Discover');
        this._discoverHandler = () => {
            Service.get('/hub/discover').then(() => {
                Notify.info('Starting device discovery');
            });
        };
        Service.socket.on('device.discovered', (msg) => {
            Notify.success('New device ' +
                (msg.name ? '\'' + msg.name + '\'' : '') +
                ' discovered'
            );
            this._state.devices++;
            this.render();
        });
   }

    update () {
        Service.get('/hub/state').then((res) => {
            this._state.mode    = res.mode;
            this._state.devices = res.devices;
            this._state.version = res.version;
            this.render();
        });
        return this;
    }

    render () {
        super.render();
        this._stateButton
            .val(Hub.mode(this._state.mode))
            .render();


        this._$el
            .height(200)
            .find('.widget-body').addClass('hub-body')
            .append($('<div>').addClass('hub-icon'))
            .append(
                $('<ul>').addClass('hub-data')
                    .append($('<li>').text(`Version : ${this._state.version}`))
                    .append($('<li>').text(`Mode    : ` + Hub.mode(this._state.mode)))
                    .append($('<li>').text(`Devices : ${this._state.devices}`))
            );

        this._$el
            .find('.widget-footer')
            .append(this._discoverButton.render().$el().addClass('hub-discover-button'))
            .append(this._stateButton.$el().addClass('hub-mode-toggle'));
        this._discoverButton.click(this._discoverHandler);

        return this;
    }

}

export default Hub;
