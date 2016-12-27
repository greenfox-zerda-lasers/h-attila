// imitate the setInterval functionality with setTimeouts (recreate the previous excersize)

window.addEventListener('mousemove', function(event){
  posX = event.screenX;
  posY = event.screenY;
});

function mouseListener(){
  setTimeout(function(){
    console.log('mouse position (X: ' + posX + ', Y: ' + posY + ')');
    mouseListener();
  }, 1500);
}

mouseListener();
