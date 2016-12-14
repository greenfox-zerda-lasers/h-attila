// imitate the setInterval functionality with setTimeouts (recreate the previous excersize)

var poyX, posY;

window.addEventListener('mousemove', function(event){
  posX = event.screenX;
  posY = event.screenY;

});

var mouseCoordinates = function(){
    window.setTimeout(function(){
        console.log('event: ', posX, posY);
        mouseCoordinates();
    }, 1500);
};

mouseCoordinates();
