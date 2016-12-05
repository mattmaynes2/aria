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
    }
    render () {

        this._$el
            .empty()
            .addClass('device-view-body')
            .append([
                this._name.render().state(this._state.name).$el(),
                this._maker.render().state(this._state.deviceType.maker).$el(),
                this._protocol.render().state(this._state.deviceType.protocol).$el()
            ]);

        return this;
    }
}

export default DeviceView;
