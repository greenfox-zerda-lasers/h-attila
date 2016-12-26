var http = require('http');

var server = http.createServer(function (req, res) {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  var d = new Date();
  res.end('Hey! How are you? Your url:' + req.url + ', methold: ' + req.method + ', date: ' + d.getFullYear() + '.' + d.getMonth() + '.' + d.getDate());
});


server.listen(3000, '127.0.0.1');
