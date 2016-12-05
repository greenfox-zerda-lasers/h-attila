'use strict';

var o = "pneumonoultramicroscopicsilicovolcanoconiosis";
// tell how many letters o has
var result = 0;
for (var i=0; i<=o.length; i++){
  if (o[i] === 'o'){
    result++
  }
}
console.log('number of "o"-s in string: ', result);
