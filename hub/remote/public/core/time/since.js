import Component from '../component';

import './since.css';

class Since extends Component {
    constructor (state) {
        super();
        state = state || '';
        this._state = isNaN(state) ? new Date(state) : new Date(parseInt(state));
    }
    render () {
        this._$el.addClass('time-since');
        updateTime.call(this);
        return this;
    }
    remove () {
        this._state = null;
        super.remove();
        return this.
    }
}

let TimeInterval = {
    DECA    : 10,
    MINUTE  : 60,
    HOUR    : 3600,
    DAY     : 86400
};

function updateTime () {
    if (!this._state) {return false;}

    let delta = secondsSince(this._state);
    this._$el.attr('title', this._state.toLocaleString());

    if (delta < TimeInterval.DECA) {
        this._$el.text('now');
        setTimeout(updateTime.bind(this), TimeInterval.DECA * 1000);
    }
    else if (delta < TimeInterval.MINUTE) {
        this._$el.text('' + Math.floor(delta) + 's');
        setTimeout(updateTime.bind(this), TimeInterval.DECA * 1000);
    }
    else if (delta < TimeInterval.HOUR) {
        this._$el.text('' + Math.floor(delta / TimeInterval.MINUTE) + 'm');
        setTimeout(updateTime.bind(this), TimeInterval.MINUTE * 1000);
    }
    else if (delta < TimeInterval.DAY) {
        this._$el.text('' + Math.floor(delta / TimeInterval.HOUR) + 'h');
        setTimeout(updateTime.bind(this), TimeInterval.HOUR * 1000);
    }
    else {
        this._$el.text(this._state.toDateString());
    }
}

function secondsSince (timestamp) {
    return (Date.now() - timestamp.getTime()) / 1000;
}

export default Since;
