// 'use strict';

// Create a constructor for creating Animals.
// it should take one parameter: what the animal says
// Every animal should have a method called say() that prints what the animal says

function Animal(sound){
  this.says = function(){
    console.log(sound);
  };
}

var cat = new Animal('meaouh!');
var dog = new Animal('vaouuh!');
var partyCarrot = new Animal('Hello! I\'m a party parrot!');

cat.says();
dog.says();
partyCarrot.says();
