var fs      = require('fs')
    exec    = require('child_process').execSync;

function run (manifest, cmd) {
    Object.keys(manifest).forEach((target) => {
        if (manifest[target][cmd]) {
            console.log(`Executing '${cmd}' on target '${target}'`);
            exec(`cd ${__dirname} && ` + manifest[target][cmd], (error, stdout, stderr) => {
                if (error) {
                    console.error(`exec error: ${error}`);
                    return;
                  }
                  console.log(stdout);
                  console.log(stderr);
            });
        }
    });
};


run(JSON.parse(fs.readFileSync(process.argv[2])), process.argv[3])

