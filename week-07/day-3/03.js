//'use strict';

// write a function called each that takes an array and a function as a paramter
// and calls the function with each element of the array as parameter
// so it should call the array 3 times if the array has 3 elements

var newArray = ['1', '2', '3'];

function eachArray(myArray, myFunction){
  myArray.forEach(function(item, index, arr) {
    myFunction(item, index, arr)
  })
}


eachArray(newArray, console.log);
