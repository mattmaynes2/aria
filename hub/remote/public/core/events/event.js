import $            from 'jquery';
import Component    from '../component';
import DeviceIcon   from '../device/icon';

import './event.css';

class Event extends Component {
    constructor (event) {
        super();
        this._state = event || {
            index       : 0,
            timestamp   : '',
            source      : '',
            device      : '',
            deviceType  : '',
            attribute   : '',
            datatype    : '',
            value       : ''
        };

        if (event) {
            this._state.timestamp = new Date(event.timestamp + ' UTC');
        }
        this._icon = new DeviceIcon(this._state.deviceType);
    }
    render () {
        this._$body = $('<div>')
            .addClass('event-body')
            .append([
                $('<div>').addClass('event-info').text(this._state.device),
                $('<div>').addClass('event-info').text(this._state.attribute),
                $('<div>').addClass('event-info').text(this._state.value)
            ]);

        this._$time = $('<div>').addClass('event-time');
        this._$el
            .empty()
            .addClass('event-frame')
            .append([this._icon.render().$el().addClass('event-icon'), this._$body, this._$time]);

        updateTime.call(this);
        return this;
    }
}

let TimeInterval = {
    DECA    : 10,
    MINUTE  : 60,
    HOUR    : 3600,
    DAY     : 86400
};

function updateTime () {
    if (!this._state.timestamp) {return false;}

    let delta = secondsSince(this._state.timestamp);
    this._$time.attr('title', this._state.timestamp.toLocaleString());

    if (delta < TimeInterval.DECA) {
        this._$time.text('now');
        setTimeout(updateTime.bind(this), TimeInterval.DECA * 1000);
    }
    else if (delta < TimeInterval.MINUTE) {
        this._$time.text('' + Math.floor(delta) + 's');
        setTimeout(updateTime.bind(this), TimeInterval.DECA * 1000);
    }
    else if (delta < TimeInterval.HOUR) {
        this._$time.text('' + Math.floor(delta / TimeInterval.MINUTE) + 'm');
        setTimeout(updateTime.bind(this), TimeInterval.MINUTE * 1000);
    }
    else if (delta < TimeInterval.DAY) {
        this._$time.text('' + Math.floor(delta / TimeInterval.HOUR) + 'h');
        setTimeout(updateTime.bind(this), TimeInterval.HOUR * 1000);
    }
    else {
        this._$time.text(this._state.timestamp.toDateString());
    }
}

function secondsSince (timestamp) {
    return (Date.now() - timestamp.getTime()) / 1000;
}

export default Event;
