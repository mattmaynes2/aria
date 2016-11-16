var fs      = require('fs'),
    spawn   = require('child_process').spawn;


var Timer = (function () {

    function Timer () {
        this._start = [0, 0];
        this._end = [0, 0];
    }

    Timer.prototype.start = function () {
        this._start = process.hrtime();
        return this;
    };

    Timer.prototype.stop = function () {
        this._end = process.hrtime(this._start);
        return this;
    };

    Timer.prototype.seconds = function () {
        return this._end[0] + (this._end[1] / 1000000000);
    };

    Timer.prototype.milliseconds = function () {
        return (this._end[0] * 1000) + (this._end[1] / 1000000);
    };

    Timer.prototype.microseconds = function () {
        return (this._end[0] * 1000000) + (this._end[1] / 1000);
    };

    return Timer;
} ());

var CPUClock = (function () {

    function CPUClock () {
        this._timer = new Timer();
        this._start = {};
        this._end = {};
    }

    CPUClock.prototype.start = function () {
        this._timer.start();
        this._start = process.cpuUsage();
        return this;
    };

    CPUClock.prototype.stop = function () {
        this._timer.stop();
        this._end = process.cpuUsage(this._start);
    };

    CPUClock.prototype.usage = function () {
        var ms = this._timer.microseconds();
        return {
            user    : this._end.user / ms,
            system  : this._end.system / ms
        };
    };

    CPUClock.prototype.active = function () {
        return this._end.user + this._end.system;
    };

    CPUClock.prototype.idle = function () {
        return this._timer.microseconds() - this.active();
    };

    return CPUClock;
} ());

var ProcStat = (function () {

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

function columnify (table) {
    var columns = Object.keys(table[0]),
        widths  = columns.reduce((w, column) => {
            w[column] = 1 + maxLength(table, column);
            return w;
        }, {}),
        spacedColumns = columns.map((column) => {
            var name = column.toString().toUpperCase();
            return name + Array(widths[column] - name.length).join(' ');
        }),
        header = '| ' + spacedColumns.join(' | ') + ' |\n| ' + spacedColumns.map((c) => {
            return Array(1 + c.length).join('-');
        }).join(' | ') + ' |\n';

    return header + table.map((row) => {
        return '| ' + columns.map((column) => {
            var cell = (row[column] || '').toString();
            return cell + Array(widths[column] - cell.length).join(' ');
        }).join(' | ') + ' |';
    }).join('\n');
}

function maxLength (table, column) {
    return Math.max(column.length, table.reduce((m, row) => {
        return Math.max((row[column] || '').toString().length, m);
    }, 0));
}

function shellJoin (cmd) {
    return Array.isArray(cmd) ? cmd.join(' && ') : cmd;
}

function execute (manifest, directive, targets, options) {
    var target      = targets[0],
        cmd         = shellJoin(manifest[target][directive]),
        fullcmd     = `cd ${__dirname} && ` + cmd,
        stat        = new ProcStat(target),
        child;

    options         = options || {};
    options._stats  = options._stats || [];
    options._stats.push(stat);
    console.log(`Executing '${directive}' on target '${target}'`);

    try {
        stat.start();
        child = spawn(fullcmd, [], { shell : true });

        if (!options.quiet) {
            child.stdout.on('data', (data) => { process.stdout.write(data); });
            child.stderr.on('data', (data) => { process.stderr.write(data); });
        }

        child.on('close', (code) => {
            stat.stop();
            if (code !== 0) {
                console.error(`Process terminated with code ${code}`);
                process.exit(1);
            }
            else if (targets.length > 1) {
                execute(manifest, directive, targets.slice(1), options);
            }
            else if (options.stats) {
                console.log(columnify(options._stats.map((s) => { return s.data(); })));
            }

        });
    } catch (e) {
        console.error(`Executing '${directive}' on target '${target}' failed`);
        console.error(e);
        process.exit(1);
    }
}


function run (manifest, directive, target, options) {
    var targets;

    options = options || {};
    targets = Object.keys(manifest).filter((x) => {
        return target ? target === x : true;
    }).filter((target) => { return !!manifest[target][directive]; });

    execute(manifest, directive, targets, options);
}

var manPath     = process.argv[2],
    directive   = process.argv[3],
    target      = process.argv[4],
    manifest    = JSON.parse(fs.readFileSync(manPath));

run(manifest, directive, target, {
    stats   : true,
    quiet   : false
});
