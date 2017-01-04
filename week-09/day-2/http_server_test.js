var http = require('http');

var server = http.createServer(function (req, res) {
  console.log('request url: ' + req.url);
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Hello, my name is Server!');
});

server.listen(3000, '127.0.0.1');
console.log('Hello, server is running and listening on port: 3000');
