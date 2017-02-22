import $                from 'jquery';
import Component        from '../component';
import DeviceIcon       from '../device/icon';
import DeviceAttribute  from '../device/attribute';
import Since            from '../time/since';
import Field            from '../control/field';

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
            attribute   : {},
        };

        this._time      = new Since(this._state.timestamp);
        this._icon      = new DeviceIcon(this._state.deviceType);
        this._device    = new Field('', { label : this._state.device });
        this._attribute = new DeviceAttribute(this._state.attribute);
    }
    
    render () {
        this._$body = $('<div>')
            .addClass('event-body')
            .append([
                this._device.render().$el(),
                this._attribute.render().$el()
            ]);

        this._$el
            .empty()
            .addClass('event-frame')
            .append([
                this._icon.render().$el().addClass('event-icon'),
                this._$body,
                this._time.render().$el()
            ]);

        return this;
    }
}
export default Event;
