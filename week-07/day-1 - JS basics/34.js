'use strict';

var ag = [3, 4, 5, 6, 7];
// double all the element's values in ag

ag.forEach(function(item, index){
  ag[index] *= 2;
});

console.log(ag);
