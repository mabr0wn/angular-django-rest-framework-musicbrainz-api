const BundleTracker = require('webpack-bundle-tracker');
const path = require('path');


module.exports = {
    output: {
        "path":  path.join(process.cwd(), "dist"),
        "filename":  "[name].bundle.js",
        "chunkFilename":  "[id].chunk.js",
        "crossOriginLoading":  false,
        "publicPath":"http://localhost:4200/"//1
    },
    "devServer": {
        "historyApiFallback":  true,
        "publicPath":  "http://localhost:4200/",//2
    },
    plugins: [
        new BundleTracker({ filename: '../webpack-stats.json' })
    ]
}