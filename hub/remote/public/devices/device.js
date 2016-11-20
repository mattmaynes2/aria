import uuid     from 'react-native-uuid';
import Widget   from './widget';


class Device extends Widget {
    constructor () {
        super();
        this._state = {
            id      : uuid.unparse(new Array(16).fill(0)),
            title   : 'Device',
            name    : '',
            address : uuid.unparse(new Array(16).fill(0))
        };
    }
    render () {
        super.render();
    }
}
/*
function fetchDevices () {
    $.ajax({
        url     : '/request',
        type    : 'POST',
        data    : '{"action" : "list_devices"}',
        headers : {
            'Content-Type' : 'application/json'
        }
    }).done((res) => {

        this._$el.find('.widget-body').empty().text(res);
    });
}
*/
export default Device;

