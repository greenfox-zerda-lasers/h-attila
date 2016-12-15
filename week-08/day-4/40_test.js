var test = require('tape');
var stringToAppendA = require('./40.js');
console.log(stringToAppendA);

test('string append to a', function(t){
  var actual = stringToAppendA('alm');
  var excepted = 'alma';
  t.equal(actual, excepted);
  t.end();
});
