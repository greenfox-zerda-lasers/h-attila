// 'use strict'

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference

function Rectangle(a, b){
  this.getArea = function(){
    return a*b;
  };
  this.getCircumference = function(){
    return 2*(a+b);
  };
}

var newRectangle_1 = new Rectangle(2, 3);
var newRectangle_2 = new Rectangle(5, 10);

console.log(newRectangle_1.getArea());
console.log(newRectangle_1.getArea());

console.log(newRectangle_1.getCircumference());
console.log(newRectangle_2.getCircumference());
