import $ from 'jquery';

class Component {
    constructor (state, props) {
        this._state = state || {};
        this._props = props || {};
        this._listeners = {
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
        this._$el.remove();
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
        this._props = props;
        return this;
    }
    change (observer) {
        this._listeners.change.push(observer);
        return this;
    }
    click (observer) {
        this._listeners.click.push(observer);
        return this;
    }
    _changed (custom) { notify.call(this, this._listeners.change, custom); }
    _clicked (custom) { notify.call(this, this._listeners.click, custom);  }
}

function notify (V, e) {
    V.forEach((v) => { v(this._state, this, e); });
}

export default Component;

