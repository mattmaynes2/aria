import $                from 'jquery';
import Component        from '../component';
import DeviceParameter  from './parameter';
import DataType         from './data-type';

import './attribute.css';

class DeviceAttribute extends Component {
    constructor (state, props) {
        super();
        this._state = {
            name        : state.name || 'Unknown Attribute',
            parameters  : state.parameters || []
        };
        this._props = props || { isControllable : false };
    }

    render () {

        this._parameters = this._state.parameters.map((param) => {
            return this._props.isControllable ?
                new DeviceParameter(param.value, param) :
                new DataType(param.value, param);
        });

        this._parameters.forEach((param, i) => {
            param.change((state) => {
                this._state.parameters[i].value = state;
                this.trigger('change', this._state.parameters[i]);
            });
        });

        this._$parameters = $('<div>').addClass('device-params')
            .append(this._parameters.map((param) => {
                return param.render().$el();
            }));


        this._$el
            .empty()
            .addClass('device-attribute')
            .append($('<div>').text(this._state.name).addClass('device-attribute-name'))
            .append(this._$parameters);
        return this;
    }
}

export default DeviceAttribute;

