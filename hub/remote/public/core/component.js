import $ from 'jquery';

class Component {
    constructor (state, props) {
        this._state = state || {};
        this._props = props || {};
        this._observers = {
            change  : [],
            click   : [],
        };
        this._$el = $('<div>');
    }
    update (state) {
        this.state(state);
        return this;
    }
    render () {
        return this;
    }
    remove () {
        this._clickObserver = null;
        if (this._$el) { this._$el.remove(); }
        return this;
    }
    $el (el) {
        if (arguments.length === 0) {
            return this._$el;
        }
        this._$el = el;
        return this;
    }
    state (state) {
        if (arguments.length === 0) {
            return this._state;
        }
        this._state = state;
        return this;
    }
    props (props) {
        if (arguments.length === 0) {
            return this._props;
        }
        this._props = $.extend(this._props || {}, props);
        return this;
    }
    change (observer) {
        if (this._observers.change.indexOf(observer) === -1) {
            this._observers.change.push(observer);
        }
        return this;
    }
    click (observer) {
        if (!this._clickObserver) {
            this._clickObserver = this._click.bind(this);
        } else {
            this._$el.off(this._clickObserver);
        }
        this._$el.click(this._clickObserver);

        if (this._observers.click.indexOf(observer) === -1) {
            this._observers.click.push(observer);
        }
        return this;
    }
    trigger (event, custom) {
        let id = '_' + event;

        if (this[id]) { this[id](custom); }
        return this;
    }
    _change (custom) {
        notify.call(this, this._observers.change, custom);
    }
    _click (custom) {
        notify.call(this, this._observers.click, custom);
    }
}

function notify (V, e) {
    V.forEach((v) => { v(this._state, this, e); });
}

export default Component;

