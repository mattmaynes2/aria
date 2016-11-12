module.exports = {
    entry   :  __dirname + '/src/index.js',
    output  : {
        path        : __dirname + '/bin',
        filename    : 'app.bundle.js',
    },
    module  : {
        loaders : [
            {
                test    : /\.js$/,
                exclude : /node_modules/,
                loader  : 'babel-loader'
            },
            {
                test    : /\.css$/,
                loader  : 'style-loader!css-loader'
            },
            {
                test    : /\.png$/,
                loader  : 'url-loader?limit=100000'
            },
            {
                test    : /\.jpg$/,
                loader  : 'file-loader'
            }
        ]
    }
};
