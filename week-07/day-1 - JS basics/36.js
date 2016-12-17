'use strict';

var ah = [3, 4, 5, 6, 7];
// print the sum of all numbers in ah

var sum = 0;
ah.forEach(function(number){
  sum += number;
});

console.log(sum);
