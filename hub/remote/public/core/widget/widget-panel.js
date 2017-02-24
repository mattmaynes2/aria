import Component from '../component';
import './widget-panel.css';

class WidgetPanel extends Component {
    constructor () {
        super();
        this._widgets = [];
    }

    _prerender () {
        this._$el.addClass('widget-panel').empty();

        this._widgets.forEach(this.append.bind(this));
        return this;
    }

    addWidget (widget) {
        this._widgets.push(widget);
        return this;
    }

    clearWidgets () {
        this._widgets = [];
        return this;
    }
}

export default WidgetPanel;
