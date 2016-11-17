let Timer       = require('./timer'),
    CPUClock    = require('./cpuclock');

let ProcStat = (function () {

    function ProcStat (target) {
        this._target = target;
        this._timer = new Timer();
        this._cpu   = new CPUClock();
    }

    ProcStat.prototype.start = function () {
        this._cpu.start();
        this._timer.start();
        return this;
    };

    ProcStat.prototype.stop = function () {
        this._cpu.stop();
        this._timer.stop();
    };

    ProcStat.prototype.data = function () {
        var secs = this._timer.seconds();

        // TODO cpu usage is no tracking the child process
        // usage = this._cpu.usage();

        return {
            target      : this._target,
            runtime     : Math.round(1000 * secs) / 1000
        };
    };

    return ProcStat;
} ());

module.exports = ProcStat;
