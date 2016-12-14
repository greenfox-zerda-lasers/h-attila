// set up a setInterval loop with 1.5 second delays
// - log the mouse coordinates on each call

var poyX, posY;

window.addEventListener('mousemove', function(event){
  posX = event.screenX;
  posY = event.screenY;

});

var mouseCoordinates = function(){
  window.setInterval(function(){
    console.log('event: ', posX, posY);
  }, 1500);
};


mouseCoordinates();
