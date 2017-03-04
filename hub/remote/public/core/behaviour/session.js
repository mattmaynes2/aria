import Component from '../component';

class Session extends Component {
    constructor (state, props) {
        super(state, props);
        this._state = {
            id          : this._state.id            || 0,
            name        : this._state.name          || '',
            created     : this._state.createdDate   || 0
        };
    }

    _prerender () {
        this.text(this._state.name);
        return this;
    }

}

export default Session;
