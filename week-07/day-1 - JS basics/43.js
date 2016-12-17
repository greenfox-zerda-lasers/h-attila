// 'use strict';

var numbers = [3, 4, 5, 6, 7, 8];
// write a function that filters the odd numbers
// from an array and returns a new array consisting
// only the evens

function oddNumbers (numbers){
  var newArr = [];
  numbers.forEach(function(number){
    if (number%2 === 0){
      newArr.push(number);
    }
  });
  return newArr;
}

function oddNumbersWithFilter (numbers){
  var newArr2 = numbers.filter(function(number){
    return number%2 === 0;
  });
  return newArr2;
}


console.log(oddNumbers(numbers));
console.log(oddNumbersWithFilter(numbers));
