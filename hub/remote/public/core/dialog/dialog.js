import $            from 'jquery';
import Component    from '../component';
import Button       from '../control/button';

import './dialog.css';

class Dialog extends Component {

    constructor (state, props) {
        super(state, props);
        this._props = {
            title   : this._props.title     || '',
            buttons : this._props.buttons   || [],
            close   : this._props.close === undefined ? true : this._props.close,
            classes : 'dialog'
        };
    }

    _prerender () {
        $(document).append(this._$el);

        this._buttons = new Component().addClass('dialog-buttons').append(
            this._props.buttons.map((text) => {
                return new Button(text);
            })
        );

        if (this._props.cancel) {
            this._buttons.push(new Button('Cancel')
                .click(this.remove.bind(this)));
        }

        this.append([
            new Component().addClass('dialog-title').text(this._props.title),
            new Component().addClass('dialog-body').append(this._state)
        ]);

        return this;
    }

}

// TODO TESTING ONLY! //
window.Dialog = Dialog;
window.Component = Component;

export default Dialog;
