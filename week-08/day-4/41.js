// 'use strict';

var numbers = [4, 5, 6, 7, 8, 9, 10];
var number = 5;
// write your own sum function

function mySum(numbers){
  var sum = 0;
  numbers.forEach(function(item){
    sum += item;
  });
  return sum;
}

// console.log(mySum(number));
module.exports = mySum;
