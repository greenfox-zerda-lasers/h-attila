// Add a click event listener to a <button> and console.log its innerHTML

var myButton = document.querySelector('button');
myButton.addEventListener('click', function(event){
  console.log(this.innerHTML);
});
