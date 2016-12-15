var test = require('tape');
var numberDubler = require('./39.js');


test('double input numbers', function(t){
  var actual = numberDubler(123);
  var excepted = 246;
  t.equal(actual, excepted);
  t.end();
});
