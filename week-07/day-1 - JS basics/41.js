'use strict';

var numbers = [4, 5, 6, 7, 8, 9, 10]
// write your own sum function

function mySum(numbers){
  var i=0;
  var sum=0;
  while(i<numbers.length){
    sum += numbers[i];
    i++;
  }
  return sum;
}

console.log(mySum(numbers));
