let Timer = require('./timer');

let ProcStat = (function () {

    function ProcStat (target) {
        this._target = target;
        this._timer = new Timer();
    }

    ProcStat.prototype.start = function () {
        this._timer.start();
        return this;
    };

    ProcStat.prototype.stop = function () {
        this._timer.stop();
    };

    ProcStat.prototype.data = function () {
        var secs = this._timer.seconds();

        return {
            target      : this._target,
            runtime     : Math.round(1000 * secs) / 1000
        };
    };

    return ProcStat;
} ());

module.exports = ProcStat;
