import WidgetPanel  from '../core/widget/widget-panel';
import Service      from '../core/service/service';
import Behaviour       from '../core/behaviour/behaviour';

class TrainingPanel extends WidgetPanel {
    constructor () {
        super();
        this._state = {
            behaviours: []
        };
    }
    update () {
        Service.set('/hub/training/behaviours', { start: 0, count: 10}).then((res) => {
            this._state.behaviours = res.payload.records.map((b) => {
                return new Behaviour(b);
            });
            this.render();
        });
        return this;
    }
    render () {
        this._$el
            .append(this._state.behaviours.map((b) => {
                return b.render().$el();
            }));
        return this;
    }

}

export default TrainingPanel;
