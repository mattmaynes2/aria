import $ from 'jquery';
import Component from '../component';

import './color-picker.css';

class ColorPicker extends Component {
    constructor (color) {
        super();
        this._state = color || '000000';
        this._$el = $('<input>').prop('type', 'color');
    }
    state (state) {
        if (arguments.length === 0) {
            return this._state;
        }
        this._state = removeHash(state);
        return this;
    }
    render () {
        this._$el
            .empty()
            .val(addHash(this._state))
            .change((e) => {
                this.state(removeHash(this._$el.val()));
                this.trigger('change', e);
            });
        return this;
    }
}

function addHash (color) {
    return typeof color !== 'string' ? '' : color.charAt(0) === '#' ? color : '#' + color;
}

function removeHash (color) {
    return typeof color !== 'string' ? '' : color.charAt(0) === '#' ? color.slice(1) : color;
}

export default ColorPicker;
