import $ from 'jquery';

class Component {
    constructor (state) {
        this._state = state || {};
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
}

export default Component;

