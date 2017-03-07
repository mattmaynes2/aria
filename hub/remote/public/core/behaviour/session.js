import Widget from '../widget/widget';

class Session extends Widget {
    constructor (state, props) {
        super(state, props);
        this._state = {
            id          : this._state.id            || 0,
            title       : this._state.name          || '',
            created     : this._state.createdDate   || 0
        };
    }

}

export default Session;
