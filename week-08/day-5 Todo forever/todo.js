var addButton = document.querySelector('.button');
addButton.addEventListener('click', function(){
  if (addButton.id == 'close'){
    addButton.id = '';
  } else {
    addButton.id = 'close';
  }
});
