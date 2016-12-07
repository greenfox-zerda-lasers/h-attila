// 'use strict';

// Create a `Stack` constructor that stores elements
// It should have a `size` method that returns number of elements it has
// It should have a `push` method that adds an element to the stack
// It should have a `pop` method that returns the last element form the stack and also deletes it from it

// please don`t use the built in methods


function Stack() {
  this.elements = ['1', '2', '3'];

  this.size = function(){
    return this.elements.length;
  };

  this.push = function(item){
    this.elements[this.elements.length] = item;
  };

  this.pop = function(){
    var lastElement = this.elements[this.elements.length-1];
    var newArr = [];
    for (var i=0; i<this.elements.length-1; i++){
      newArr[i] = this.elements[i];
    }
    this.elements = newArr;
    return lastElement;
  };
}

myArray = new Stack();

console.log(myArray.size());
myArray.push('4');
console.log(myArray.size());
myArray.push('5');
console.log(myArray.pop());
console.log(myArray.elements);
