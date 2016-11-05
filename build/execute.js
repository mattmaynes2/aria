var fs      = require('fs'),
    spawn   = require('child_process').spawn;

function shellJoin (cmd) {
    return Array.isArray(cmd) ? cmd.join(' && ') : cmd;
}

function execute (manifest, directive, targets) {
    var target      = targets[0],
        cmd         = shellJoin(manifest[target][directive]),
        fullcmd     = `cd ${__dirname} && ` + cmd,
        child;

    console.log(`Executing '${directive}' on target '${target}'`);

    try {
        child = spawn(fullcmd, [], { shell : true });
        child.stdout.on('data', (data) => { process.stdout.write(data); });
        child.stderr.on('data', (data) => { process.stderr.write(data); });
        child.on('close', (code) => {
            if (code !== 0) {
                console.error(`Process terminated with code ${code}`);
                process.exit(1);
            }
            else if (targets.length > 1) {
                execute(manifest, directive, targets.slice(1));
            }
        });
    } catch (e) {
        console.error(`Executing '${directive}' on target '${target}' failed`);
        console.error(e);
        process.exit(1);
    }
}


function run (manifest, directive, target) {
    var targets = Object.keys(manifest).filter((x) => {
        return target ? target === x : true;
    }).filter((target) => { return !!manifest[target][directive]; });

    execute(manifest, directive, targets);
}

var manPath     = process.argv[2],
    directive   = process.argv[3],
    target      = process.argv[4],
    manifest    = JSON.parse(fs.readFileSync(manPath));

run(manifest, directive, target);
