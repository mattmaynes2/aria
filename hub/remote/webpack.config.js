let loaders = {
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
    };


module.exports = {
    entry   : {
        'hub'       : __dirname + '/public/hub/index.js',
        'devices'   : __dirname + '/public/devices/index.js',
        'stats'     : __dirname + '/public/stats/index.js',
        'schedule'  : __dirname + '/public/schedule/index.js',
        'training'  : __dirname + '/public/training/index.js'
    },
    output  : {
        path        : __dirname + '/public/',
        filename    : '[name]/[name].bundle.js',
    },
    module : loaders,
    devtool: '#inline-source-map'
};
