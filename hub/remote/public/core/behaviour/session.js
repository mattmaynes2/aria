import Widget from '../widget/widget';
import SessionView from './session-view';
import SessionControl from './session-control';

import './session.css';

class Session extends Widget {
    constructor (state, props) {
        super(state, props);
        this._state = {
            id          : this._state.id            || 0,
            title       : this._state.name          || '',
            createdDate : this._state.createdDate   || 0,
            stopped     : this._state.stopped       || 0
        };

        this._view = new SessionView(this._state, this._props);
        this._control = new SessionControl(this._state, this._props);
    }

    render () {
        super.render();

        this._$el
            .find('.widget-body').addClass('session-body')
            .append([
                this._view.addClass('session-info').render().$el(),
                this._control.addClass('session-buttons').render().$el()
            ]);
        return this;
    }
}

export default Session;
