// SETTING UP SERVER COMMUNICATION
var talkToServer = (method, additionalUrl, data, callbackFunc) => {
  const url = 'http://localhost:3000' + additionalUrl;
  const httpRequest = new XMLHttpRequest();
  httpRequest.open(method, url, true);
  httpRequest.setRequestHeader('Content-Type', 'application/json; charset=utf-8');
  httpRequest.send(data);
  httpRequest.onreadystatechange = function () {
    if (httpRequest.readyState === XMLHttpRequest.DONE) {
      callbackFunc(JSON.parse(httpRequest.response));
    }
  };
};

// GET DATA FROM WEB
var list = () => {
  talkToServer('GET', '/todos', '', updateTodoList);
};

// UPDATE DATA STATUS ON WEB
var update = (id, status, text) => {
  const data = JSON.stringify({ text: text, completed: status });
  talkToServer('PUT', '/todos/' + id, data, list);
};

// ADD NEW TODO DATA TO WEB
var add = (newTodoText) => {
  const data = JSON.stringify({ text: newTodoText });
  talkToServer('POST', '/todos', data, list);
};

// DELETE TODO DATA FROM WEB
var deleteTodo = (id) => {
  const data = JSON.stringify({});
  talkToServer('DELETE', '/todos/' + id, data, list);
};

// ADD BUTTON CREATE
var addButton = document.querySelector('.button');
addButton.addEventListener('click', () => {
  var inputFieldText = document.querySelector('.inputField');
  var newTodoText = inputFieldText.value;
  inputFieldText.value = '';
  add(newTodoText);
});

// CREATE AND DISPLAY TODO LIST
var updateTodoList = (response) => {
  this.todoText = '';
  var todoListElement = document.querySelector('ul');
  response.forEach((listItem) => {
    this.todoText += '<li><div class="todo-text">' + listItem.text + '</div><div id="' + listItem.id + '" class="todo-dashbin"> </div><div id="' + listItem.id + '" class="todo-check"> </div></li>';
  }, this);
  todoListElement.innerHTML = this.todoText;

  // CHECKBOX EVENT HANDLING
  var checkBoxes = document.querySelectorAll(".todo-check");
  checkBoxes.forEach((item, index) => {
    if (response[index].completed === false) {
      item.className = 'todo-check';
    } else {
      item.className = 'todo-checked';
    }
    item.addEventListener('click', () => {
      update(item.id, !response[index].completed, response[index].text);
    });
  });

  // DELETE BUTTON EVENT HANDLING
  var checkBin = document.querySelectorAll('.todo-dashbin');
  checkBin.forEach((item) => {
    item.addEventListener('click', () => {
      deleteTodo(item.id);
    });
  });
};

// STYLE SETTINGS
var settingsMenu = document.querySelector('.settings');
var stylesheet = document.querySelector('#stylesheet');
var stylechecker = 0;

settingsMenu.addEventListener('click', () => {
  var styleList = ['css/todo.css', 'css/todo_1.css', 'css/todo_2.css'];
  stylechecker += 1;
  if (stylechecker >= 3) {
    stylechecker = 0;
  }
  stylesheet.href = styleList[stylechecker];
});

// START MAIN FUNCTION
list();
