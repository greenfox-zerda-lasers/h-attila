//'use strict';

// write a function called each that takes an array and a function as a paramter
// and calls the function with each element of the array as parameter
// so it should call the array 3 times if the array has 3 elements

newArray = [1, 2, 3, 4, 5];

function each(arr, myFunction){
  result = [];
  arr.forEach(function(item){
    result.push(myFunction(item));
  });
  return result;
}

function dubler(number){
  return number * 2;
}

console.log(each(newArray, dubler));
