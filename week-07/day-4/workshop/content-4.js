var newItemsForList = ['apple', 'banana', 'cat', 'dog'];
var linksInTheDocument = document.querySelectorAll('li');
for (i=0; i<linksInTheDocument.length; i++){
  linksInTheDocument[i].innerHTML = newItemsForList[i];
}
