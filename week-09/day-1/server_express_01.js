var express = require('express');

var app = express();
app.get('*', function (req, res) {
  var date = new Date();
  res.send('request url: ' + req.url + ', request methold: ' + req.method + ', date: ' + date);
});

app.listen(3000);
