import Component    from '../component';
import Field        from '../control/field';

import './add-session.css';

class AddSession extends Component {
    constructor (state, props) {
        super(state, props);
        this._state = {
            name            : this._state.name || '',
            behaviourId     : this._state.behaviourId || 0
        };
        this.addClass('add-session');
    }

    state (state) {
        if (arguments.length === 0) {
            return {
                name        : this._nameField.state(),
                behaviourId : this._state.behaviourId
            };
        }
        this._nameField.state(state);
        return this;
    }

    _prerender () {
        this._nameField = new Field(this._state.name, { label : 'Name: ' , editable : true});

        this.append(this._nameField);
        return this;
    }
}

export default AddSession;
