import $ from 'jquery';
import Component from '../component';

import './color-picker.css';

class ColorPicker extends Component {
    constructor (color) {
        super();
        this._state = color || '000000';
        this._$el = $('<input>').prop('type', 'color');
    }
    render () {
        this._$el.val(this._state);
        return this;
    }
}

export default ColorPicker;
