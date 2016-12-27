// create a function that when called alerts "I'm delayed" after 1 second

function alerts(time){
  window.setTimeout(function(){
    alert("I'm delayed!");
  }, time);
}

alerts(1000);
