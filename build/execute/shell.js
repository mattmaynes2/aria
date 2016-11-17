let spawn       = require('child_process').spawn,
    columnify   = require('./columnify'),
    ProcStat    = require('./procstat');

function shellJoin (cmd) {
    return Array.isArray(cmd) ? cmd.join(' && ') : cmd;
}

function processClose (manifest, directive, stat, targets, options, code) {
    stat.stop();
    if (code !== 0) {
        console.error(`Process terminated with code ${code}`);
        process.exit(1);
    }
    else if (targets.length > 1) {
        shell(manifest, directive, targets.slice(1), options);
    }
    else if (options.stats) {
        console.log(columnify(options._stats.map((s) => { return s.data(); })));
    }
}

function shell (manifest, directive, targets, options) {
    var target      = targets[0],
        cmd         = shellJoin(manifest[target][directive]),
        fullcmd     = `cd ${__dirname}/../ && ` + cmd,
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

        child.on('close', processClose.bind(null, manifest, directive, stat, targets, options));
    } catch (e) {
        console.error(`Executing '${directive}' on target '${target}' failed`);
        console.error(e);
        process.exit(1);
    }
}

module.exports = shell;
