var test = require('tape');
var mySum = require('./41.js');

test('my sum function test', function(t){
  var actual = mySum([4, 5, 6, 7, 8, 9, 10]);
  var excepted = 49;
  t.equal(actual, excepted);
  t.end();
});

test('my sum test with one list number', function(t){
  var actual = mySum([5]);
  var excepted = 5;
  t.equal(actual, excepted);
  t.end();
});


test('my sum test with one number', function(t){
  t.throws(function(){mySum(5)}, TypeError);
  t.end();
});
