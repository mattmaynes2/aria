import Component    from '../component';
import Field        from '../control/field';

class SessionView extends Component {
    constructor (state, props) {
        super(state, props);
    }
    _prerender () {
        this.clear().append(
            new Field(new Date(this._state.createdDate).toLocaleString(), { label : 'Created: ' })
        );
        return this;
    }
}

export default SessionView;
