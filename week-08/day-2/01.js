// create a function that when called alerts "I'm delayed" after 1 second

var myAlert = function(){
  window.setTimeout(function(){
    alert("I'm delayed");
  }, 1000);
};

myAlert();
