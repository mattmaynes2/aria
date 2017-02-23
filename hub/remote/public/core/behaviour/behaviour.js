import Widget           from '../widget/widget';
import BehaviourView       from './view';

import './behaviour.css';

class Behaviour extends Widget {
    constructor (state) {
        super();
        state = state || {};

        this._state = {
            name        : state.name        || 'Unnamed',
        };

        this._view = new BehaviourView(this._state);
    }
    render () {
        super.render();

        this._$el
            .find('.widget-body').addClass('behaviour-body')
            .append(
                this._view.render().$el().addClass('behaviour-info')
            );
        return this;
    }
}

export default Behaviour;

