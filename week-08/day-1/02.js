// 'use strict'

// Create a constructor for creating Rectangles.
// it should take two parameters: the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference

function Rectangle(a, b) {
  this.a = a;
  this.b = b;
};

Rectangle.prototype.getArea = function() {
  return this.a * this.b;
};

Rectangle.prototype.getCircumference = function () {
  return 2*(this.a + this.b);
};

var rect_1 = new Rectangle(10, 2);
console.log(rect_1.getArea());
console.log((rect_1.getCircumference()));

var rect_2 = new Rectangle(10, 10);
console.log(rect_2.getArea());
console.log(rect_2.getCircumference());
