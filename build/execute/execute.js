let fs      = require('fs'),
    shell   = require('./shell');

function run (manifest, directive, target, options) {
    var targets;

    options = options || {};
    targets = Object.keys(manifest).filter((x) => {
        return target ? target === x : true;
    }).filter((target) => { return !!manifest[target][directive]; });

    shell(manifest, directive, targets, options);
}

var manPath     = process.argv[2],
    directive   = process.argv[3],
    target      = process.argv[4],
    manifest    = JSON.parse(fs.readFileSync(manPath));

run(manifest, directive, target, {
    stats   : true,
    quiet   : false
});
