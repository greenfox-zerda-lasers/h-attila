// ***** button click for future *****
var addButton = document.querySelector('.button');

addButton.addEventListener('click', function(){
  var inputFieldText = document.querySelector('.inputField');
  console.log(inputFieldText.value);
  app.add(inputFieldText.value);
});

// ***** APP object create *****
function APP(){}

APP.prototype.open = function (){
  var httpRequest = new XMLHttpRequest();
  httpRequest.open('GET', 'https://mysterious-dusk-8248.herokuapp.com/todos');
  httpRequest.send();
  httpRequest.onreadystatechange = function(){
    if (httpRequest.readyState === XMLHttpRequest.DONE){
      var response = JSON.parse(httpRequest.response);
      app.list(response);
    }
  };
};

APP.prototype.list = function(response){
  var todoListElement = document.querySelector('ul');
  var todoText = "";
  response.forEach(function(listItem){
    todoText += '<li><div class="todo-text">' + listItem.text + '</div><div class="todo-dashbin"> </div><div class="todo-check"> </div></li>';
  });
  console.log(todoText);
  todoListElement.innerHTML = todoText;
};

APP.prototype.update = function(){
  console.log('update');
};

APP.prototype.add = function(item){
  todoText += '<li><div class="todo-text">' + listItem.text + '</div><div class="todo-dashbin"> </div><div class="todo-check"> </div></li>';
};

APP.prototype.delete = function(){
  console.log('delete');
};

// ***** START main function *****

var app = new APP();
app.open();
