
// 'use strict';


// create a function that takes a string and a letter and returns a boolean
// it should return true if the string consits the given letter, false otherwise

var letter = 'a';
var string_1 = 'alma';
var string_2 = 'körte';


function letterChecker (letter, string){
  return string.split('').some(function(item){
    return item === 'a';
  });
}

console.log(letterChecker(letter, string_1));
console.log(letterChecker(letter, string_2));
