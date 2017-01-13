import Component    from '../component';
import Field        from '../control/field';

import './view.css';

class DeviceView extends Component {
    constructor (device) {
        super();
        this._state = device || {};
        this._name      = new Field('', { label : 'Name:'           });
        this._maker     = new Field('', { label : 'Manufacturer:'   });
        this._protocol  = new Field('', { label : 'Protocol:'       });
        this._id        = new Field('', { label : 'Device ID:'      });
    }
    render () {

        this._$el
            .empty()
            .addClass('device-view-body')
            .append([
                this._name.state(this._state.name).render().$el(),
                this._maker.state(this._state.deviceType.maker).render().$el(),
                this._protocol.state(this._state.deviceType.protocol).render().$el(),
                this._id.state(this._state.address).render().$el()
            ]);

        return this;
    }
}

export default DeviceView;
