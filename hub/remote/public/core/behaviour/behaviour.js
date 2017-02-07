import $                from 'jquery';
import uuid             from 'react-native-uuid';
import Widget           from '../widget/widget';
import BehaviourView       from './view';
import Service          from '../service/service';
import Notify           from '../notify/notify';

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
            )
            .append(this._$attrs);
        return this;
    }
}

export default Behaviour;

