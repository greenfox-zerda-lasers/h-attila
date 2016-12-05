'use strict';

// create a function that returns it's input factorial

function myFactorial(inputNumber){
  var result = 1;
  for (var i=1; i <= inputNumber; i++){
    result *= i;
  }
  return result;
}


console.log(myFactorial(5));
