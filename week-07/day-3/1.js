// 'use strict';

// Create a function that takes a number and returns it as string in english
// like 0 -> "zero", it should work with the first 5 numbers, after it should
// return "many"

function englishNumbers(number){
  switch (number) {
    case 0:
      return 'zero';
    case 1:
      return 'one';
    case 2:
      return 'two';
    case 3:
      return 'three';
    case 4:
      return 'four';
    case 5:
      return 'five';
    default:
      return 'many';
  }
}

console.log(englishNumbers(0));
console.log(englishNumbers(1));
console.log(englishNumbers(2));
console.log(englishNumbers(3));
console.log(englishNumbers(4));
console.log(englishNumbers(5));
console.log(englishNumbers(6));
