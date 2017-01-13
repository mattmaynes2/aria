import uuid             from 'react-native-uuid';
import Widget           from '../widget/widget';
import DeviceIcon       from './icon';
import DeviceView       from './view';
import DeviceAttribute  from './attribute';

import './device.css';

class Device extends Widget {
    constructor (state) {
        super();
        state = state || {};
        state.deviceType = state.deviceType || {};

        this._state = {
            id          : state.id          || uuid.unparse(new Array(16).fill(0)),
            name        : state.name        || 'Unknown Device',
            address     : state.address     || uuid.unparse(new Array(16).fill(0)),
            deviceType  : {
                name        : state.deviceType.name     || 'Unknown Type',
                maker       : state.deviceType.maker    || 'Unknown Manufacturer',
                protocol    : state.deviceType.protocol || 'Unknown Protocol',
                attributes  : state.deviceType.attributes || []
            }
        };
        this._props = {
            controllable : false
        };

        this._state.title  = this._state.name;
        this._icon = new DeviceIcon(this._state.deviceType.name);
        this._view = new DeviceView(this._state);
    }
    render () {
        super.render();
        this._$el
            .height(200)
            .find('.widget-body').addClass('device-body')
            .append([
                this._icon.render().$el().addClass('device-icon'),
                this._view.render().$el().addClass('device-info')
            ])
            .append(this._state.deviceType.attributes.map((attr) => {
                return new DeviceAttribute(attr, this._props).render().$el();
            }));

        return this;
    }
}

export default Device;

