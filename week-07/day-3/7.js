// 'use strict';

var numbers = [2, 5, 11, 29, 3, 10];

// create a function that takes an array of numbers and returns a boolean
// it should return true if all the elements are prime, false otherwise


function primeChecker(arr){
  return arr.every(function(number){
    var result = true;
    if (number > 3){
      for (var i=2; i<number; i++){
        if (number%i === 0){
          result = false;
      }}}
    return result;
  }
);
}

console.log(primeChecker(numbers));
