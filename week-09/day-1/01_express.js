var express = require('express');

var app = express();

app.get('/user/:id/:name', function (req, res) {
  res.send('The given id is: ' + req.params.id + ', user name: ' + req.params.name);
});

app.get('/', function (req, res) {
  var d = new Date();
  res.send('Hey! How are you? Entry point: "/"; Your url:' + req.url + ', methold: ' + req.method + ', date: ' + d.getFullYear() + '.' + d.getMonth() + '.' + d.getDate());
});

app.listen(3000);
