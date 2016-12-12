// 'use strict';

// Create a constructor for creating Animals.
// it should take one parameter: what the animal says
// Every animal should have a method called say() that prints what the animal says

function Animal(talk){
  this.talk = talk;
}

Animal.prototype.says = function(){
  console.log(this.talk);
};

var parrot = new Animal('Hello, my name is party parrot!');
parrot.says();

var dog = new Animal('Wauw!')
dog.says();

var cat = new Animal('meaouh!')
cat.says();
