'use strict';

var names = ['Zakarias', 'Hans', 'Otto', 'Ole'];
// create a function that returns the shortest string
// from an array

function theShortestString(names){
  let shortest = names[0];
  names.forEach(function(name){
    if (name.length < shortest.length){
      shortest = name;
    }
  });
  return shortest;
}

console.log(theShortestString(names));
