// create a function that starts a setTimeout with a 3 second delay.
// - create a button with an event listener that can cancel the setTimeout

function bombRobber(){
  timer = window.setTimeout(function(){
    alert("You're dead!");
  }, 3000);
}

var stopButton = document.querySelector('button');
stopButton.addEventListener('click', function(){
  window.clearTimeout(timer);
  alert("You're safe now.");
});

bombRobber();
