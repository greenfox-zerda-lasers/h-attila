const express = require('express');

const app = express();

// INIT DATA AFTER START
const todoData = [
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
app.get('/todos', (req, res) => {
  res.send(todoData);
});

// RESPOND ONE TODO DATA
app.get('/todod/:id', (req, res) => {
  res.send(todoData[req.params.id - 1]);
});

// ADD NEW TODO ITEM TO TODODATA ARRAY
app.post('/todos', (req, res) => {
  let reqBody = [];
  if (todoData.length > 0) {
    let newItemId = todoData[todoData.length - 1].id + 1;
  } else {
    let newItemId = 0;
  }
  let newText = '';
  req.on('data', (chunk) => {
    reqBody.push(chunk);
  }).on('end', () => {
    reqBody = Buffer.concat(reqBody).toString();
    newText = JSON.parse(reqBody).text;
    todoData.push({ completed: false, id: newItemId, text: newText });
  });
  res.send(true);
});

// TOGGLE TODO ITEM COMPLETED
app.put('/todos/:id', (req, res) => {
  todoData.forEach((item, index) => {
    if (item.id === parseInt(req.params.id, 10)) {
      todoData[index].completed = !todoData[index].completed;
    }
  });
  res.send(true);
});

// DELETE ONE TODO ITEM
app.delete('/todos/:id', (req, res) => {
  todoData.forEach((item, index) => {
    if (item.id === parseInt(req.params.id, 10)) {
      todoData.splice(index, 1);
    }
  });
  res.send(true);
});

// START SERVER
console.log('server listening');
app.listen(3000);
