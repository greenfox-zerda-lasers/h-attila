'use strict';

// create a function that returns it's input factorial

function myFracrotial(number){
  var result = 1;
  for (var i=1; i<=number; i++){
    result *= i;
  }
  return result;
}

console.log(myFracrotial(3));
