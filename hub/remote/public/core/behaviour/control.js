import Component    from '../component';
import Button       from '../control/button';
import Dialog       from '../dialog/dialog';
import Session      from './session';
import SessionPanel from './session-panel';
import Service      from '../service/service';
import StateButton  from '../control/state-button';

import './control.css';

class BehaviourControl extends Component {
    constructor (state, props) {
        super(state, props);
        this._sessions  = new Button('Sessions').addClass('behaviour-control-button');
        this._remove    = new Button('Remove').addClass('behaviour-control-button');
        this._toggleActive = new StateButton(BehaviourControl.activeState(state.active),
             BehaviourControl.activeStates);
        this.append([this._sessions, this._remove, this._toggleActive]);
        this.addClass('behaviour-control');
        this._props.remove = this._props.remove || (() => {});
    }

    static get activeStates() {
        return ['Active', 'Inactive'];
    }

    static activeState(val) {
        if (typeof val === 'string') {
            return val === 'Active';
        }else{
            return val === true ? 'Active' : 'Inactive';
        }
    }

    static active(label) {
        return label === 'Active';
    }

    static getActive(val) {
        if (val === true) {
            return 'Active';
        }
        return 'Inactive';
    }

    _postrender () {
        this._remove.$el().off().click(remove.bind(this));
        this._sessions.$el().off().click(sessions.bind(this));
        this._toggleActive.change((state) => {
            Service.set('/hub/training/behaviour/' + this._state.id, { 
                    active: BehaviourControl.activeState(state)
                })
                .then((res) => {
                    this._state = res.payload;
                    this.render();
                });
        });
    }
}

function sessions () {
    let panel = new SessionPanel({
        sessions    : this._state.sessions.map((s) => { return new Session(s); }),
        behaviour   : this._state
    });

    new Dialog(
        panel,
        {
            title   : `${this._state.title} Sessions`,
            close   : true
        }
    ).render();

    panel.update();
}

function remove () {
    let d = new Dialog(
        `Removing behaviour '${this._state.title}' will remove all associated training ` +
        'session data. Are you sure you want to remove it?',
        {
            title   : `Remove ${this._state.title}`,
            close   : false,
            buttons : [
                {
                    text    : 'Cancel',
                    click   : () => { d.remove(); }
                },
                {
                    text    : 'Remove',
                    click   : () => {
                        Service.delete('/hub/training/behaviour/' + this._state.id)
                            .then(() => {
                                this._props.remove();
                            });
                        d.remove();
                    }
                }
            ]
        }
    ).width(400).height(200).render();
}

export default BehaviourControl;
