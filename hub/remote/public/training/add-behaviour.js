import Component    from '../core/component';
import Field        from '../core/control/field';

class AddBehaviour extends Component {
    constructor (state, props) {
        super(state, props);
        this._state = {
            name : this._state.name || ''
        };
    }

    state (state) {
        if (arguments.length === 0) {
            return {
                name : this._nameField.state()
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

export default AddBehaviour;
