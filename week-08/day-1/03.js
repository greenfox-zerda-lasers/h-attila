// 'use strict';

// Create a constructor for creating Rockets.
// it should take one parameter: the consumption of the rocket
// (amount of fuel needed for launch)
// Every rocket should have a method called fill(amount) that fills the tank of
// the rocket with the amount of fuel given as a parameter
// Every rocket should have a method called launch() that launches the rocket
// if it has enough fuel (more than its consumption)


function Rocket(consumptionPerLaunch){
  this.consumptionPerLaunch = consumptionPerLaunch;
  this.fuelAmount = 0;
  this.launches = 0;
}

Rocket.prototype.fill = function(fuelAmount){
  this.fuelAmount += fuelAmount;
  console.log('Successfull filling! Avaiable fuel:', this.fuelAmount);
};

Rocket.prototype.launch = function(){
  if (this.fuelAmount >= this.consumptionPerLaunch){
    this.launches++;
    this.fuelAmount -= this.consumptionPerLaunch;
    console.log('Launch the rocket! Remaining fuel: ' + this.fuelAmount + ', number of launches: ' + this.launches);
  }
  else {
    console.log('Not enough fuel to launch!');
  }
};

var myNewRocket_1 = new Rocket(1);
myNewRocket_1.launch();
myNewRocket_1.fill(3);
myNewRocket_1.launch();
myNewRocket_1.launch();
myNewRocket_1.launch();
myNewRocket_1.launch();
