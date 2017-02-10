import WidgetPanel  from '../core/widget/widget-panel';
import Service      from '../core/service/service';
import Behaviour    from '../core/behaviour/behaviour';
import Button      from '../core/control/button'; 
import Modal from '../core/modal/modal';

class TrainingPanel extends WidgetPanel {
    constructor () {
        super();
        this._state = {
            behaviours: []
        };
        this._behaviourModal = new Modal();
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
        var addButton = new Button('Add');
        addButton.click(()=>{
            this._behaviourModal.show();
        });
       
        this._$el.append(
            addButton.render().$el()
        );

        this._$el.append(this._behaviourModal.render().$el());

        this._$el
            .append(this._state.behaviours.map((b) => {
                return b.render().$el();
            }));
        return this;
    }

}

export default TrainingPanel;
