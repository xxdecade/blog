const path = require('path');

module.exports = {
  mode: 'production',
  entry: '../../myblog/static/js/src/base.js',
  output: {
    path: path.resolve(__dirname, '../../myblog/static/js/dist'),
    filename: 'myblog.js',
    libraryTarget: 'umd'
  }
};
