// 'use strict';

// Create a `Stack` constructor that stores elements
// It should have a `size` method that returns number of elements it has
// It should have a `push` method that adds an element to the stack
// It should have a `pop` method that returns the last element form the stack and also deletes it from it

// please don`t use the built in methods


var Stack = function(){
  this.elements = [];

  this.size = function(){
    return this.elements.length;
  };

  this.push = function(newItem){
    this.elements[this.elements.length] = newItem;
  };

  this.pop = function(){
    if (this.elements.length > 0){
      var lastItem = this.elements[this.elements.length-1];
      var newElements = [];
      for (var i=0; i<this.elements.length-1; i++){
        newElements.push(this.elements[i]);
      }
      this.elements = newElements;
      return lastItem;
    } else {
      return 'no item in the list';

    }
  };
};


var newStack = new Stack();
console.log(newStack.size());
console.log(newStack.pop());
newStack.push('hello');
newStack.push(5);
newStack.push('sziamia');
newStack.push('almatorta');
console.log(newStack.size());
console.log(newStack.pop());
console.log(newStack.size());
