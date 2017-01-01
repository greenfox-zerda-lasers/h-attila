var express = require('express');

var app = express();

// INIT DATA AFTER START
var todoData = [
  {
    completed: true,
    id: 1,
    text: '1 Buy milk',
  },
  {
    completed: false,
    id: 2,
    text: '2 Make presentation',
  },
  {
    completed: false,
    id: 3,
    text: '3 Make love',
  },
];

// INIT STATIC CONTENT
app.use('/', express.static('web'));

// RESPOND ALL TODO DATA
app.get('/todos', function (req, res) {
  res.send(todoData);
});

// RESPOND ONE TODO DATA
app.get('/todod/:id', function (req, res) {
  res.send(todoData[req.params.id - 1]);
});

// ADD NEW TODO ITEM TO TODODATA ARRAY
app.post('/todos', function (req, res) {
  var reqBody = [];
  if (todoData.length > 0) {
    var newItemId = todoData[todoData.length - 1].id + 1;
  } else {
    var newItemId = 0;
  }
  var newText = '';
  req.on('data', function (chunk) {
    reqBody.push(chunk);
  }).on('end', function () {
    reqBody = Buffer.concat(reqBody).toString();
    newText = JSON.parse(reqBody).text;
    todoData.push({ completed: false, id: newItemId, text: newText });
  });
  res.send(true);
});

// TOGGLE TODO ITEM COMPLETED
app.put('/todos/:id', function (req, res) {
  todoData.forEach(function (item, index) {
    if (item.id === parseInt(req.params.id)) {
      todoData[index].completed = !todoData[index].completed;
    }
  });
  res.send(true);
});

// DELETE ONE TODO ITEM
app.delete('/todos/:id', function (req, res) {
  todoData.forEach(function (item, index) {
    if (item.id === parseInt(req.params.id)) {
      todoData.splice(index, 1);
    }
  });
  res.send(true);
});

// START SERVER
app.listen(3000);
