var webpack     = require('webpack'),
    externals   = require('webpack-node-externals'),
    Shell       = require('webpack-shell-plugin');

var output = {
        path        : __dirname + '/bin',
        filename    : 'gateway'
    },
    outfile = output.path + '/' + output.filename;

module.exports = {
    entry       : __dirname + '/src/gateway.js',
    target      : 'node',
    externals   : [externals()],
    output      : output,
    plugins     : [
        new webpack.BannerPlugin('#!/usr/bin/env node\n', { raw : true }),
        new Shell({ onBuildEnd : ['chmod +x ' + outfile] })
    ]
};
