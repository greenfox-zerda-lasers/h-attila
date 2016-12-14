// create a function that starts a setTimeout with a 3 second delay.
// - create a button with an event listener that can cancel the setTimeout

var timer;

var myButton = document.querySelector('button');
myButton.addEventListener('click', function(){
  window.clearTimeout(timer);
});

var bombExposion = function(){
  timer = window.setTimeout(function(){
    alert('You dead!');
  }, 3000);
};


bombExposion();
