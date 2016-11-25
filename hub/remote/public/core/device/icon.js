import Component from '../component';

class DeviceIcon extends Component {
    constructor (type) {
        super();
        this._state = type || '';
    }

    render () {
        this._$el.css({
                backgroundImage     : 'url(' + guessIcon(this._state) + ')',
                backgroundSize      : 'contain',
                backgroundRepeat    : 'no-repeat',
                backgroundPosition  : 'center'
            });
        return this;
    }
}

let IconPatterns = [
    { exp : /(thermo|temp)/ , url : '/assets/devices/thermo.png' },
    { exp : /(coffee)/      , url : '/assets/devices/coffee.png' },
    { exp : /(tv|tele)/     , url : '/assets/devices/tv.png'     },
    { exp : /(music|tune)/  , url : '/assets/devices/music.png'  },
    { exp : /(switch)/      , url : '/assets/devices/switch.png' },
    { exp : /(light)/       , url : '/assets/devices/light.png'  },
    { exp : /.*/            , url : '/assets/devices/device.png' }
];

function guessIcon (type) {
    var icon;

    type = (type || '').toLowerCase();
    icon = IconPatterns.filter((pattern) => {
        return pattern.exp.test(type);
    });

    return (icon[0] || IconPatterns[IconPatterns.length - 1]).url;
}

export default DeviceIcon;
