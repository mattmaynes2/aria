var webpack     = require('webpack'),
    externals   = require('webpack-node-externals');

var output = {
        path        : __dirname + '/bin',
        filename    : 'gateway'
    },
    config = {
        entry       : __dirname + '/src/gateway.js',
        target      : 'node',
        externals   : [externals()],
        output      : output,
    };

if (process.argv.indexOf('--executable') >= 0) {
    config.plugins = [
        new webpack.BannerPlugin('#!/usr/bin/env node\n', { raw : true })
    ];
}

module.exports = config;
