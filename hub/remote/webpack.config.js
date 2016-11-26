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

function page (name) {
    name = name || '';
    return {
        entry   :  __dirname + `/public/${name}/index.js`,
        output  : {
            path        : __dirname + `/public/${name}`,
            filename    : name ? `${name}.bundle.js` : 'bundle.js',
        },
        module : loaders,
        devtool: '#inline-source-map'
    };
}

module.exports = [
    page('hub'),
    page('devices'),
    page('stats'),
    page('schedule')
];
