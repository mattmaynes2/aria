import Widget           from '../widget/widget';
import BehaviourView    from './view';
import BehaviourControl from './control';

import './behaviour.css';

class Behaviour extends Widget {
    constructor (state, props) {
        super(state, props);
        state = state || {};

        this._state = {
            title       : state.name          || 'Unknown Behaviour',
            id          : state.id            || '',
            sessions    : state.sessions      || [],
            active      : state.active        || false,
            createdDate : state.createdDate   || 0,
            lastUpdated : state.lastUpdated   || 0
        };

        this._view = new BehaviourView(this._state);
        this._control = new BehaviourControl(this._state);
    }
    render () {
        super.render();

        this._$el
            .find('.widget-body').addClass('behaviour-body')
            .append([
                this._view.render().$el().addClass('behaviour-info'),
                this._control.render().$el().addClass('behaviour-buttons')
            ]);
        return this;
    }
}

export default Behaviour;

