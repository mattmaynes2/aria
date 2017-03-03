import Component from '../component';

class Session extends Component {
    constructor (state, props) {
        super(state, props);
        this._state = {
            id          : this._state.id            || 0,
            created     : this._state.createdDate   || 0
        };

    }

}

export default Session;
