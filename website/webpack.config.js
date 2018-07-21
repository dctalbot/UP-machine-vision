const webpack = require('webpack')
const path = require('path')

const config = {
  entry: './website/javascript/index.jsx',
  output: {
    path: path.resolve(__dirname + '/website/static/', 'dist'),
    filename: 'bundle.js',
    publicPath: '/assets/'
  },
  module: {
    rules: [
      {
        test: /\.jsx?/,
        exclude: /node_modules/,
        loader: 'babel-loader'
      },
      {
        test: /\.css$/,
        use: [
          {
            loader: 'style-loader'
          },
          {
            loader: 'css-loader'
          }
        ]
      },
      {
        test: /\.(png|woff|woff2|eot|ttf|svg)$/,
        loader: 'url-loader?limit=100000'
      }
    ]
  },
  resolve: {
    extensions: ['.js', '.jsx', '.css', '.scss'],
    alias: {
      normalize: path.join(
        __dirname,
        'node_modules/normalize.css/normalize.css'
      ),
      blueprint_core: path.join(
        __dirname,
        'node_modules/@blueprintjs/core/lib/css/blueprint.css'
      ),
      blueprint_icons: path.join(
        __dirname,
        'node_modules/@blueprintjs/icons/lib/css/blueprint-icons.css'
      )
    }
  }
}
module.exports = config
