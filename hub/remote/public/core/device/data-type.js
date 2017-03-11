import Component from '../component';

import './data-type.css';

class DataType extends Component {
    static get Binary   () { return 'binary';   }
    static get Byte     () { return 'byte';     }
    static get Color    () { return 'color';    }
    static get Date     () { return 'date';     }
    static get Enum     () { return 'enum';     }
    static get Float    () { return 'float';    }
    static get List     () { return 'list';     }
    static get Integer  () { return 'int';      }
    static get String   () { return 'string';   }
    static get Time     () { return 'time';     }

    constructor (state, props) {
        super();
        this._state = state;
        if (!state && (state !== 0)) {
            this._state = '';
        }
        this._props = props || {
            dataType : ''
        };
    }
    render () {
        this._$el.addClass('device-data-type');
        switch (this._props.dataType) {
            case DataType.Binary:
                this._$el.text(this._state ? 'On' : 'Off');
                break;
            case DataType.Color:
                this._$el
                    .css('background-color', addHash(this._state).substr(0,7))
                    .css('color', brightness(this._state) > 100 ?
                        'black' : 'white'
                    )
                    .text(addHash(this._state.toUpperCase()));
                break;
            default:
                this._$el.text(this._state);
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

function addHash (color) {
    return typeof color !== 'string' ? '' : color.charAt(0) === '#' ? color : '#' + color;
}


export default DataType;
