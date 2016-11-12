import $        from 'jquery';
import Widget   from './widget';

class Hub extends Widget {

    constructor () {
        super();
        this._state.title = 'Hub';
    }

    render () {
        super.render();

        if (!this._$stateButton) {
            this._$stateButton = $('<button>').text('Refresh Status')
                .click(fetchStatus.bind(this));
            this._$el.find('.widget-footer').append(this._$stateButton);
        }

        return this;
    }

}

function fetchStatus () {
    $.ajax({
        url     : '/request',
        type    : 'POST',
        data    : '{"action" : "status"}',
        headers : {
            'Content-Type' : 'application/json'
        }
    }).done((res) => {
        this._$el.find('.widget-body').empty().text(res);
    });
}


export default Hub;
