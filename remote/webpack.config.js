module.exports = {
    entry   :  __dirname + '/src/index.js',
    output  : {
        path        : __dirname + '/bin',
        filename    : 'app.bundle.js',
    },
    module  : {
        loaders : [{
            test    : /\.js$/,
            exclude : /node_modules/,
            loader  : 'babel-loader'
        }]
    }
};
