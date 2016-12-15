// ***** button click for future *****
var addButton = document.querySelector('.button');

addButton.addEventListener('click', function(){
  var inputFieldText = document.querySelector('.inputField');
  app.add(inputFieldText.value);
});

// ***** APP object create *****
function APP(){
  this.todoText = '';
}

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
  this.todoText = "";
  response.forEach(function(listItem){
    this.todoText += '<li><div class="todo-text">' + listItem.text + '</div><div class="todo-dashbin"> </div><div class="todo-check"> </div></li>';
  }, this);
  todoListElement.innerHTML = this.todoText;
  
  var checkBoxes = document.querySelectorAll('.todo-check');
  checkBoxes.forEach(function(item, index){
    if (response[index].completed === true){
      item.style.backgroundImage = 'url("success_ok.svg")';
    } else {
      item.style.backgroundImage = 'url("oval.svg")';
    }
  });
};

APP.prototype.update = function(){
  console.log('update');
};

APP.prototype.add = function(item){
  dataToUpload = {};
  dataToUpload.text = item;

  var httpPost = new XMLHttpRequest();
  httpPost.open('POST', 'https://mysterious-dusk-8248.herokuapp.com/todos');
  httpPost.setRequestHeader('Content-Type', 'application/json');
  httpPost.send(JSON.stringify(dataToUpload));
  httpPost.onreadystatechange = function(){
    if (httpPost.readyState === XMLHttpRequest.DONE){
      app.open();
    }
  };
};

APP.prototype.delete = function(item){
  console.log('delete');
  dataToUpload = 'https://mysterious-dusk-8248.herokuapp.com/todos/' + item;

  var httpPost = new XMLHttpRequest();
  httpPost.open('DELETE', dataToUpload);
  httpPost.setRequestHeader('Content-Type', 'application/json');
  httpPost.send();
  app.open();
};

// ***** START main function *****

var app = new APP();
app.open();
