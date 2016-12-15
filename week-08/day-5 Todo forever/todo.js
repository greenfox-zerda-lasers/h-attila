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
      var response = JSON.parse(httpRequest.response).reverse();
      app.list(response);
    }
  };
};

APP.prototype.list = function(response){
  var todoListElement = document.querySelector('ul');
  this.todoText = "";
  response.forEach(function(listItem){
    this.todoText += '<li><div class="todo-text">' + listItem.text + '</div><div id="' + listItem.id + '" class="todo-dashbin"> </div><div id="' + listItem.id + '" class="todo-check"> </div></li>';
  }, this);
  todoListElement.innerHTML = this.todoText;
  var checkBoxes = document.querySelectorAll('.todo-check');
  checkBoxes.forEach(function(item, index){
    if (response[index].completed === true){
      item.style.backgroundImage = 'url("images/success_ok.svg")';
    } else {
      item.style.backgroundImage = 'url("images/oval.svg")';
    }
    item.addEventListener('click', function(){
      app.update(item.id, response[index].completed, response[index].text);
    });
  });

  var checkBin = document.querySelectorAll('.todo-dashbin');
  checkBin.forEach(function(item){
    item.addEventListener('click', function(){
      app.delete(item.id);
    });
});

APP.prototype.update = function(id, state, text){
  var dataToUpload = {};
  dataToUpload.text = text;
  if (state === true){
    dataToUpload.completed = false;
  } else {
    dataToUpload.completed = true;
  }
  console.log(dataToUpload);
  var httpPost = new XMLHttpRequest();
  httpPost.open('PUT', 'https://mysterious-dusk-8248.herokuapp.com/todos/' + id);
  httpPost.setRequestHeader('Content-Type', 'application/json');
  httpPost.send(JSON.stringify(dataToUpload));
  httpPost.onreadystatechange = function(){
    if (httpPost.readyState === XMLHttpRequest.DONE){
      app.open();
    }
  };
};
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

APP.prototype.delete = function(id){
  dataToUpload = 'https://mysterious-dusk-8248.herokuapp.com/todos/' + id;
  var httpPost = new XMLHttpRequest();
  httpPost.open('DELETE', dataToUpload);
  httpPost.setRequestHeader('Content-Type', 'application/json');
  httpPost.send();
  httpPost.onreadystatechange = function(){
    if (httpPost.readyState === XMLHttpRequest.DONE){
      app.open();
}};
};

// ***** START main function *****

var app = new APP();
app.open();
