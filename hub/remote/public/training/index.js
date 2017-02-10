import $            from 'jquery';
import Menu         from '../nav/menu';
import TrainingPanel  from './training-panel';
import './index.css';

$(document).ready(() => {
    var training = new TrainingPanel();

    $('body')
        .append(new Menu().render().$el())
        .append(training.update().$el());
});
