// GET DATA FROM WEB
  var list = function () {
    talkToServer('GET', '/todos', '', updateTodoList);
  };

// UPDATE DATA STATUS ON WEB
  var update = function (id, status, text) {
    const data = JSON.stringify({ text: text, completed: status });
    talkToServer('PUT', '/todos/' + id, data, list);
  };

// ADD NEW TODO DATA TO WEB
  var add = function (newTodoText) {
    const data = JSON.stringify({ text: newTodoText });
    talkToServer('POST', '/todos', data, list);
  };

// DELETE TODO DATA FROM WEB
  var deleteTodo = function (id) {
    const data = JSON.stringify({});
    talkToServer('DELETE', '/todos/' + id, data, list);
  };

// SETTING UP SERVER COMMUNICATION
  var talkToServer = function (method, additionalUrl, data, callbackFunc) {
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

// ADD BUTTON CREATE
  var addButton = document.querySelector('.button');
  addButton.addEventListener('click', function () {
    var inputFieldText = document.querySelector('.inputField');
    var newTodoText = inputFieldText.value;
    inputFieldText.value = '';
    add(newTodoText);
  });

// CREATE AND DISPLAY TODO LIST
  var updateTodoList = function (response) {
    this.todoText = '';
    var todoListElement = document.querySelector('ul');
    response.forEach(function (listItem) {
      this.todoText += '<li><div class="todo-text">' + listItem.text + '</div><div id="' + listItem.id + '" class="todo-dashbin"> </div><div id="' + listItem.id + '" class="todo-check"> </div></li>';
    }, this);
    todoListElement.innerHTML = this.todoText;

// CHECKBOX EVENT HANDLING
  var checkBoxes = document.querySelectorAll(".todo-check");
  checkBoxes.forEach(function (item, index) {
    if (response[index].completed === false) {
      item.className = 'todo-check';
    } else {
      item.className = 'todo-checked';
    }
    item.addEventListener('click', function () {
      update(item.id, !response[index].completed, response[index].text);
    });
  });

// DELETE BUTTON EVENT HANDLING
  var checkBin = document.querySelectorAll('.todo-dashbin');
  checkBin.forEach(function (item) {
    item.addEventListener('click', function () {
      deleteTodo(item.id);
    });
  });
  };

// STYLE SETTINGS
  var settingsMenu = document.querySelector('.settings');
  var stylesheet = document.querySelector('#stylesheet');
  var stylechecker = 0;

  settingsMenu.addEventListener('click', function () {
    var styleList = ['css/todo.css', 'css/todo_1.css', 'css/todo_2.css'];
    stylechecker += 1;
    if (stylechecker >= 3) {
      stylechecker = 0;
    }
    stylesheet.href = styleList[stylechecker];
  });

// START MAIN FUNCTION
  list();
