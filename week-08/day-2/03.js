// set up a setInterval loop with 1.5 second delays
// - log the mouse coordinates on each call


window.addEventListener('mousemove', function(event){
  posX = event.screenX;
  posY = event.screenY;
});

window.setInterval(function(){
  console.log('mouse position (X: ' + posX + ', Y: ' + posY + ')');
}, 1500);
