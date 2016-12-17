'use sttict';

var numbers = [7, 5, 8, -1, 2];
// Write a function that returns the minimal element
// in an array (your own min function)

function myMinimal(numbers){
  var minimal = numbers[0];
  numbers.forEach(function(number){
    if (number < minimal){
      minimal = number;
    }
  });
  return minimal;
}

console.log(myMinimal(numbers));
