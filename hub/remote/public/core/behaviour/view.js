import Component    from '../component';
import Field        from '../control/field';

import './view.css';

class BehaviourView extends Component {
    constructor (state, props) {
        super(state, props);
    }
    _prerender () {
        this.clear().append(
            new Field(new Date(this._state.createdDate).toLocaleString(), { label : 'Created: ' })
        )
        .append(
            new Field(new Date(this._state.lastUpdated).toLocaleString(), { label : 'Updated: ' })
        );
        return this;
    }
}

export default BehaviourView;
