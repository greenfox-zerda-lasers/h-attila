'use sttict';

var numbers = [7, 5, 8, -1, 2];
// Write a function that returns the minimal element
// in an array (your own min function)


function minimalNumber(array){
  var minimal = array[0];
  for (var i=0; i<array.length; i++){
    if (array[i] < minimal){
      minimal = array[i];
    }
  }
  return minimal;
}

console.log(minimalNumber(numbers));
