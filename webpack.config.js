//require our dependencies
var path = require('path');
var webpack = require('webpack');
var CleanWebpackPlugin = require('clean-webpack-plugin');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  //the base directory (absolute path) for resolving the entry option
  context: __dirname,

  //the entry point we created earlier. Note that './' means
  //your current directory. You don't have to specify the extension  now,
  //because you will specify extensions later in the `resolve` section
  entry: {
    //reactApp: './reactapp/js/app',
    property_registration: './vueapp/js/property_registration/main',
    host_registration: './vueapp/js/host_registration/main',
    dashboard: './vueapp/js/dashboard/main',
  },

  output: {
    //where you want your compiled bundle to be stored
    path: path.resolve('./build/bundles/'),

    //naming convention webpack should use for your files
    filename: '[name].js',

    publicPath: '/static/bundles/'
  },

  plugins: [
    new CleanWebpackPlugin(['./build/bundles/']),

    //change the default local for ElementUI to English
    new webpack.NormalModuleReplacementPlugin(/element-ui[\/\\]lib[\/\\]locale[\/\\]lang[\/\\]zh-CN/, 'element-ui/lib/locale/lang/en'),
    new webpack.NormalModuleReplacementPlugin(/element-react[\/\\]src[\/\\]locale[\/\\]lang[\/\\]zh-CN/, 'element-react/src/locale/lang/en'),

    //tells webpack where to store data about your bundles.
    new BundleTracker({filename: './webpack-stats.json'}),

    //makes jQuery available in every module
    //new webpack.ProvidePlugin({
    //  $: 'jquery',
    //  jQuery: 'jquery',
    //  'window.jQuery': 'jquery'
    //})
  ],

  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader'
      },
      {
        test: /\.jsx?$/,
        loader: 'babel-loader',
        exclude: /node_modules/,
        query: {
          //specify that we will be dealing with React code
          presets: ['es2015', 'stage-0', 'react']
        }
      },
      {
        test: /(\.scss|\.css)$/,
        loaders: ['style-loader', 'css-loader', 'sass-loader'],
      },
      {
        test: /\.(eot|svg|ttf|woff|woff2)(\?\S*)?$/,
        loader: 'file-loader'
      },
      {
        test: /\.(jpe?g|png|gif|svg)(\?\S*)?$/,
        loader: 'file-loader',
        query: {
          name: '[name].[ext]?[hash]'
        }
      }
    ]
  },

  resolve: {
    //tells webpack where to look for modules
    modules: ['node_modules'],

    //extensions that should be used to resolve modules
    extensions: ['.vue', '.js', '.jsx']
  }
};