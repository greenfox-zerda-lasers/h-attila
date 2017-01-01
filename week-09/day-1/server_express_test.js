var express = require('express');

var talkToServer = express();

talkToServer.get('/', function (req, res) {
  res.send('Hello, this is the main page');
});

talkToServer.get('/contact', function (req, res) {
  res.send('Hello, this is the contact page');
});

talkToServer.get('/profile/:id/:name', function (req, res) {
  res.send('Hello, this is profile of id: ' + req.params.id + ', name: ' + req.params.name);
});

talkToServer.get('/image', function (req, res) {
  res.sendFile(__dirname + '/nature.jpg');
});

talkToServer.get('/dataquery', function (req, res) {
  console.log(req.query);
});

talkToServer.listen(3000);
