//'use strict';

// Create a constructor for creating Rockets.
// it should take one parameter: the consumption of the rocket
// (amount of fuel needed for launch)
// Every rocket should have a method called fill(amount) that fills the tank of
// the rocket with the amount of fuel given as a parameter
// Every rocket should have a method called launch() that launches the rocket
// if it has enough fuel (more than its consumption)

function Rocket(consumption){
  this.consumption = consumption;
  this.fuel = 0;
  this.launchCounter = 0;

  this.fill = function(amount){
    this.fuel += amount;
    console.log('Avaiable fuel: ' + this.fuel);
  };

  this.launch = function(){
    if (this.fuel >= this.consumption){
      this.fuel -= this.consumption;
      this.launchCounter++;
      console.log('Launch successfull! Fuel: ' + this.fuel + ', launches: ' + this.launchCounter);
    } else {
      console.log('Not enough fuel!');
    }
  };
}

var myRocket_1 = new Rocket(5);
myRocket_1.launch();
myRocket_1.fill(10);
myRocket_1.launch();
myRocket_1.launch();
myRocket_1.launch();
