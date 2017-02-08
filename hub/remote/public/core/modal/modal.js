import Component from '../component';
import './modal.css';
import Button from '../control/button'
import WidgetPanel from '../widget/widget-panel.js';

class Modal extends WidgetPanel {
    constructor () {
        super();

        var button = new Button('X');
        button._$el.addClass('close');
        button.click(()=>{
            this._$el.hide();
        });
        super.addWidget(button);
    }

    render() {
        this._$el.addClass('modal-dialog');
        this._$el.addClass('modal-content');

        super.render();
        return this;
    }

    hide() {
        this._$el.hide();
    }

    show() {
        this._$el.show();       
    }
}

export default Modal;