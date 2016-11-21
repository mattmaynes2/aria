import uuid     from 'react-native-uuid';
import Widget   from '../core/widget/widget';


class Device extends Widget {
    constructor (state) {
        super();
        state = state || {};
        this._state = {
            id      : state.id      || uuid.unparse(new Array(16).fill(0)),
            title   : state.name    || 'Device',
            address : state.address || uuid.unparse(new Array(16).fill(0))
        };
    }
    render () {
        super.render();
        this._$el
            .height(200);
        return this;
    }
}

export default Device;

