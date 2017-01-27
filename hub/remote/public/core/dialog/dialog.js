import $            from 'jquery';
import Component    from '../component';
import Button       from '../button/button';

import './dialog.css';

class Dialog extends Component {

    constructor (state, props) {
        super(state, props);
        this._props = {
            title   : this._props.title     || '',
            buttons : this._props.buttons   || [],
            close   : this._props.close === undefined ? true : this._props.close
        };
    }
    render () {

        this._buttons = this._props.buttons.map((text) => {
            return new Button(text);
        });

        if (this._props.cancel) {
            this._buttons.append(new Button('Cancel')
                .click(this.remove.bind(this)));
        }

        this._$title = $('<div>').addClass('dialog-title').text(this._props.title);
        this._$body  = $('<div>').addClass('dialog-body').append(this._state);

        this._$buttons = $('<div>')
            .addClass('dialog-buttons')
            .append(this._buttons.map((button) => {
                return button.render().$el();
            }));

        this._$el
            .empty()
            .addClass('dialog')
            .append([this._$title, this._$body, this._$buttons]);
    }

}

export default Dialog;
