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
            close   : this._props.close === undefined ? true : this._props.close
        };
    }

    _prerender () {

        $('body')
            .append($('<div>').addClass('dialog-wall'))
            .append(this._$el)
            .addClass('dialog-lock');

        this.addClass('dialog');

        this._closeButton = new Component().addClass('dialog-close');
        this._buttons = new Component().addClass('dialog-buttons');

        if (this._props.close) {
            this._props.buttons.push({ text : 'Close', click : this.remove.bind(this) });
        }

        this._buttons.append(
            this._props.buttons.map((button) => {
                return new Button(button.text).addClass('dialog-button');
            })
        );

        this._header = new Component().addClass('dialog-header');
        this._body = new Component().addClass('dialog-body');
        this.append([
            this._header,
            this._body,
            new Component().addClass('dialog-footer').append(this._buttons)
        ]);

        return this;
    }

    _postrender () {
        this._buttons.children().forEach((button, i) => {
            button.click(this._props.buttons[i].click);
        });

        if (this._state instanceof Component) {
            this._body.append(this._state).render();
        }
        else if (typeof this._state === 'string') {
            this._text = new Component().addClass('dialog-text');
            this._body.append(this._text).render();
            this._text.text(this._state);
        }

        this._header.text(this._props.title).append(this._closeButton);
        this._closeButton.text('x').click(this.remove.bind(this));
    }

    remove () {
        super.remove();
        $('body').removeClass('dialog-lock');
        $('.dialog-wall').remove();
    }
}

export default Dialog;
