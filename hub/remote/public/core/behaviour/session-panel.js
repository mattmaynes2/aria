import Component        from '../component';
import WidgetPanel      from '../widget/widget-panel';
import Service          from '../service/service';
import Button           from '../control/button';
import Dialog           from '../dialog/dialog';
import Session          from '../behaviour/session';
import AddSession       from './add-session';

import './session-panel.css';

class SessionPanel extends WidgetPanel {
    constructor (state, props) {
        super(state, props);
        this._state = {
            behaviour   : this._state.behaviour || {},
            sessions    : this._state.sessions  || []
        };
        this.addClass('session-panel');
    }

    update () {
        Service.get('/hub/state').then((res) => {
            var session = res.payload.session || {};
            Service.get('/hub/training/sessions', {
                start           : 0,
                count           : 10,
                behaviourId     : this._state.behaviour.id
            }).then((res) => {
                this._state.sessions = res.payload.records.map((s) => {
                    if (s.id === session.id) {
                        return new Session(s, { isActive : true }).addClass('session-active');
                    }
                    return new Session(s, { hideButtons : !!session.id });
                });
                this.render();
            });
        });
        return this;
    }

    _prerender () {
        this.clear();
        this._buttonBar = new Component().addClass('session-button-bar');
        this._newButton = new Button('New');

        this.clearWidgets();
        this.append(this._buttonBar);

        this._state.sessions.forEach(this.addWidget.bind(this));
        this._buttonBar.append(this._newButton);

        super._prerender();
        return this;
    }

    _postrender () {
        this._newButton.click(newSession.bind(this));
        return this;
    }
}


function newSession () {
    let session = new AddSession({
            name        : '',
            behaviourId : this._state.behaviour.id
        }),
        dialog  = new Dialog(session,
            {
                title   : 'New Session',
                buttons : [
                    {
                        text    : 'Create',
                        click   : () => {
                            addSession.call(this, session);
                            dialog.remove();
                        }
                    }
                ]
            }).render().height(200).width(400);
}


function addSession (session) {
    Service.set('/hub/training/session', session.state())
        .then((res) => {
            var s = new Session(res.payload);
            this._state.sessions.push(s);
            this.render();
        });
}

export default SessionPanel;
