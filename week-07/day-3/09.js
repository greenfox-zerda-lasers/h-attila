// 'use strict';

// create a function that takes a string and counts its letters
// it should return an object thats keys are the letters and the values are
// the counts.
// example: "apple" -> {a: 1, p: 2, l: 1, e: 1}


function stringCounter(myString){
  var result = {};
  myString.split('').forEach(function(item){
    if (item in result){
      result[item] += 1;
    }
    else {
      result[item] = 1;
    }
  });
  return result;
}


var magicString = 'apple';

console.log(stringCounter(magicString));
