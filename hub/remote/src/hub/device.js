import $ from 'jquery';
import Widget from './widget';

class Device extends Widget {
    constructor () {
        super();
        this._state.title = 'Device';
    }
    render () {
        super.render();
        if (!this._$deviceButton) {
            this._$deviceButton = $('<button>').text('List Devices')
                .click(fetchDevices.bind(this));
            this._$el.find('.widget-footer').append(this._$deviceButton);
        }
        return this;
    }
}

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

export default Device;

