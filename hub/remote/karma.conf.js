// Karma configuration

var webpack = require('./webpack.config');

module.exports = function(config) {
    config.set({

        // base path that will be used to resolve all patterns (eg. files, exclude)
        basePath: '',

        // frameworks to use
        frameworks: ['jasmine'],

        // list of files / patterns to load in the browser
        files: [
            'node_modules/babel-polyfill/dist/polyfill.js',
            'src/**/*.js',
            'test/**/*.spec.js'
        ],

        // list of files to exclude
        exclude: [],

        preprocessors: {
            'src/**/*.js'   : ['webpack'],
            'test/**/*.js'  : ['webpack']
        },
        webpack : webpack,
        webpackMiddleware: {
            stats: 'errors-only'
        },
        // test results reporter to use
        // possible values: 'dots', 'progress'
        // available reporters: https://npmjs.org/browse/keyword/karma-reporter
        reporters: ['progress'],

        // web server port
        port: 9876,

        // enable / disable colors in the output (reporters and logs)
        colors: true,

        // level of logging
        logLevel: config.LOG_INFO,

        // enable / disable watching file and executing tests whenever any file changes
        autoWatch: false,

        plugins : [
            'karma-jasmine',
            'karma-phantomjs-launcher',
            'karma-webpack'
        ],

        // start these browsers
        browsers: ['PhantomJS'],

        // Continuous Integration mode
        // if true, Karma captures browsers, runs the tests and exits
        singleRun: true,

        // Concurrency level
        // how many browser should be started simultaneous
        concurrency: Infinity
    });
};
