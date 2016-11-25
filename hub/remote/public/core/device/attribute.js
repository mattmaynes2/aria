import $            from 'jquery';
import Component    from '../component';
import DataType     from './data-type';

import './attribute.css';

class DeviceAttribute extends Component {
    constructor (state) {
        super();
        this._state = {
            name        : state.name || 'Unknown Attribute',
            parameters  : state.parameters || []
        };
    }

    render () {
        this._$el
            .empty()
            .addClass('device-attribute')
            .append($('<div>').text(this._state.name).addClass('device-attribute-name'))
            .append(this._state.parameters.map((param) => {
                return new DataType(param).render().$el();
            }));
        return this;
    }
}

export default DeviceAttribute;

