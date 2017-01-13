import WidgetPanel  from '../core/widget/widget-panel';
import Service      from '../core/service/service';
import Device       from '../core/device/device';

class DevicePanel extends WidgetPanel {
    constructor () {
        super();
        this._state = {
            devices : []
        };
    }
    update () {
        Service.get('/device/list').then((res) => {
            this._state.devices = res.devices.map((dev) => {
                return new Device(dev).props({ controllable : true });
            });
            this.render();
        });
        return this;
    }
    render () {
        this._$el
            .append(this._state.devices.map((dev) => {
                return dev.render().$el();
            }));


        return this;
    }

}

export default DevicePanel;
