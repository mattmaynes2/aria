import Component    from './component';
import './widget-panel.css';

class WidgetPanel extends Component {
    constructor () {
        super();
        this._widgets = [];
    }

    render () {
        this._$el.addClass('widget-panel').empty();

        this._widgets.forEach((widget) => {
            this._$el.append(widget.render().$el());
        });

        return this;
    }

    addWidget (widget) {
        this._widgets.push(widget);
    }

}

export default WidgetPanel;
