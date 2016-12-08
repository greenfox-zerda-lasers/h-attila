var newText = document.querySelectorAll('p');
for (var i=0; i < newText.length; i++){
  newText[i].textContent = newText[newText.length-1].textContent;
}
