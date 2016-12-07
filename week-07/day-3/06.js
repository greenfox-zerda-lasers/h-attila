// 'use strict';


// create a function that takes a string and a letter and returns a boolean
// it should return true if the string consits the given letter, false otherwise


function letterChecker (myString, myLetter) {
  // return myString.split('').some(function(element){
  //   return element === myLetter;
  // });
  return myString.split('').indexOf(myLetter) == -1
}


console.log(letterChecker('alma', 'x'));
console.log(letterChecker('alma', 'a'));
