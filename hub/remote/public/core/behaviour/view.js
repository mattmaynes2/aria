import Component    from '../component';
import Field        from '../control/field';

import './view.css';

class BehaviourView extends Component {
    constructor (state) {
        super();
        this._state = state || {};
        this._name  = new Field('', { label : 'Name: ' });
    }

    render () {
        this._$el
            .empty()
            .addClass('behaviour-view-body')
            .append(
                this._name.state(this._state.name).render().$el()
            );

        return this;
    }
}

export default BehaviourView;
