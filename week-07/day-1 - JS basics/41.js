'use strict';

var numbers = [4, 5, 6, 7, 8, 9, 10]
// write your own sum function

function mySum(inputList){
  var result = 0;
  for (var i=0; i<inputList.length; i++){
    result += inputList[i];
  }
  return result;
}

console.log(mySum(numbers));
