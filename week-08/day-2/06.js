// Add an event listener to the window and display the mouse's x, y coordinates

var p = document.querySelector('p');
window.addEventListener('mousemove', function(event){
  p.innerHTML = 'mouse coordinates (X: ' + event.screenX + ', Y: ' + event.screenY + ')';
});
