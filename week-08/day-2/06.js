// Add an event listener to the window and display the mouse's x, y coordinates

var textContent = document.querySelector('p');

window.addEventListener('mousemove', function(event){
  textContent.innerHTML = 'Coordinates: ' + event.screenX + ', ' + event.screenY;
});
