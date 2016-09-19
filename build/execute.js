var fs      = require('fs'),
    exec    = require('child_process').execSync;

function shellJoin (cmd) {
    return Array.isArray(cmd) ? cmd.join(' && ') : cmd;
}

function execute (manifest, directive, target) {
    var cmd         = shellJoin(manifest[target][directive]),
        fullcmd     = `cd ${__dirname} && ` + cmd;

    console.log(`Executing '${directive}' on target '${target}'`);

    try {
        exec(fullcmd, (error, stdout, stderr) => {
            console.log(stdout);
            console.log(stderr);
        });

    } catch (e) {
        console.error(`Executing '${directive}' on target '${target}' failed`);
        console.error(e.stdout.toString('utf-8'));
        console.error(e.stderr.toString('utf-8'));
        process.exit(1);
    }
}


function run (manifest, directive, target) {
    Object.keys(manifest).filter((x) => {
        return target ? target === x : true;
    }).forEach((target) => {
        if (manifest[target][directive]) {
            execute(manifest, directive, target);
        }
    });
}

var manPath     = process.argv[2],
    directive   = process.argv[3],
    target      = process.argv[4],
    manifest    = JSON.parse(fs.readFileSync(manPath));

run(manifest, directive, target);
