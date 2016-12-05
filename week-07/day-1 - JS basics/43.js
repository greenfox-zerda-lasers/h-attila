'use strict';

var numbers = [3, 4, 5, 6, 7];
// write a function that filters the odd numbers
// from an array and returns a new array consisting
// only the evens


function evenArrayMaker(inputArray){
  var newArray = [];
  for (var i=0; i<inputArray.length; i++){
    if (inputArray[i]%2 === 0){
      newArray.push(inputArray[i]);
    }
  }
  return newArray;
}

console.log(evenArrayMaker(numbers));
