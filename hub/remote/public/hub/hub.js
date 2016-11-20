import $        from 'jquery';
import Widget   from '../core/widget/widget';
import './hub.css';

class Hub extends Widget {

    constructor () {
        super();
        this._state = {
            title   : 'Smart Hub',
            version : '',
            mode    : 'Normal',
            devices : 0
        };
    }

    update () {
         $.ajax({
            url     : '/hub/state',
            type    : 'GET',
            headers : {
                'Content-Type' : 'application/json'
            }
        }).done((res) => {
            let content = JSON.parse(res).payload;
            this._state.mode    = content.mode;
            this._state.devices = content.devices;
            this._state.version = content.version;
            this.render();
        });
        return this;
    }
    render () {
        super.render();

        this._$el
            .height(200)
            .find('.widget-body').addClass('hub-body')
            .append($('<div>').addClass('hub-icon'))
            .append(
                $('<ul>').addClass('hub-data')
                    .append($('<li>').text(`Version : ${this._state.version}`))
                    .append($('<li>').text(`Mode    : ${this._state.mode}`))
                    .append($('<li>').text(`Devices : ${this._state.devices}`))
            );

        this._$el
            .find('.widget-footer')
            .append(this._logButton.$el().addClass('hub-log-button'));

        return this;
    }

}

export default Hub;
