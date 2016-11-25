import uuid         from 'react-native-uuid';
import Widget       from '../core/widget/widget';
import DeviceIcon   from '../core/device/icon';

import './device.css';

class Device extends Widget {
    constructor (state) {
        super();
        state = state || {};
        state.deviceType = state.deviceType || {};

        this._state = {
            id          : state.id          || uuid.unparse(new Array(16).fill(0)),
            title       : state.name        || 'Unknown Device',
            address     : state.address     || uuid.unparse(new Array(16).fill(0)),
            deviceType  : {
                name        : state.deviceType.name     || 'Unknown Type',
                maker       : state.deviceType.maker    || 'Unknown Manufacturer',
                protocol    : state.deviceType.protocol || 'Unknown Protocol',
                attributes  : state.deviceType.attributes || []
            }
        };
        this._icon = new DeviceIcon(this._state.deviceType.name);
    }
    render () {
        super.render();
        this._$el
            .height(200)
            .find('.widget-body').addClass('device-body')
            .append(this._icon.render().$el().addClass('device-icon'));

        return this;
    }
}

export default Device;

