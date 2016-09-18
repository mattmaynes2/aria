var fs      = require('fs'),
    exec    = require('child_process').execSync;

function execute (manifest, cmd, target) {
    var fullcmd = `cd ${__dirname} && ` + manifest[target][cmd];

    console.log(`Executing '${cmd}' on target '${target}'`);

    try {
        exec(fullcmd, (error, stdout, stderr) => {
            console.log(stdout);
            console.log(stderr);
        });

    } catch (e) {
        console.error(`Executing '${cmd}' on target '${target}' failed`);
        console.error(e.stdout.toString('utf-8'));
        console.error(e.stderr.toString('utf-8'));
        process.exit(1);
    }
}


function run (manifest, cmd, target) {
    Object.keys(manifest).filter((x) => {
        return target ? target === x : true;
    }).forEach((target) => {
        if (manifest[target][cmd]) {
            execute(manifest, cmd, target);
        }
    });
}

run(JSON.parse(fs.readFileSync(process.argv[2])), process.argv[3], process.argv[4]);

