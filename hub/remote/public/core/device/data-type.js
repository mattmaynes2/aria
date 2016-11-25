import Component from '../component';

import './data-type.css';

class DataType extends Component {
    constructor (state) {
        super();
        state = state || {};
        this._state = {
            dataType    : state.dataType    || '',
            value       : state.value       || ''
        };
    }
    render () {
        this._$el.addClass('device-data-type');
        switch (this._state.dataType) {
            case 'binary':
                this._$el.text(this._state.value ? 'On' : 'Off');
                break;
            case 'color':
                this._$el
                    .css('background-color', '#' + this._state.value)
                    .css('color', brightness(this._state.value) > 40 ?
                        'black' : 'white'
                    )
                    .text('#' + this._state.value.toUpperCase());
                break;
            default:
                this._$el.text(this._state.value);
                break;
        }
        return this;
    }
}

function brightness (color) {
    var rgb = parseInt(color, 16),
        r = (rgb >> 16) & 0xff,  // extract red
        g = (rgb >>  8) & 0xff,  // extract green
        b = (rgb >>  0) & 0xff;  // extract blue

    return  0.2126 * r + 0.7152 * g + 0.0722 * b; // per ITU-R BT.709
}

export default DataType;
