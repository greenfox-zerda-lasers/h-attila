// Create a constructor for creating Aircrafts,
// and one for creating Carriers,
// based on the specification in the python exam: https://github.com/greenfox-academy/zerda-exam-python-retake

function Aircraft(type) {
  this.ammo = 0;
  this.type = type;

  if (this.type === 'F16'){
    this.maxAmmo = 8;
    this.baseDamage = 30;
  } else if (this.type === 'F35'){
    this.maxAmmo = 12;
    this.baseDamage = 50;
  }
  console.log('Type ' + this.type + ', Ammo: ' + this.ammo + ', Base Damage: ' + this.baseDamage + ', All Damage: ' + this.maxAmmo * this.baseDamage);
}

Aircraft.prototype.fight = function(){
  let fullPower = this.ammo * this.baseDamage;
  this.ammo = 0;
  return fullPower;
};

Aircraft.prototype.refill = function(refilledAmmo){
  let unUsedAmmo = 0;
  this.ammo += refilledAmmo;
  if (this.ammo > this.maxAmmo){
    unUsedAmmo = this.ammo - this.maxAmmo;
    this.ammo = this.maxAmmo;
  }
  return unUsedAmmo;
};


function Carrier() {
  this.aircraftsInHangar = [];
  this.ammoStorage = 2800;
  this.healthRemaining = 720;
}

Carrier.prototype.add_aircraft = function(newAircraft){
  this.aircraftsInHangar.push(newAircraft);
};

Carrier.prototype.status_report = function(){
  var totalDamage = this.aircraftsInHangar.reduce(function(sum, aircraftsInHangar){
    return sum + aircraftsInHangar.baseDamage * aircraftsInHangar.ammo;
  }, 0);

  if (this.healthRemaining <= 0){
    console.log("It's dead, Jim! :(");
  } else {
  console.log('Aircrafts count: ' + this.aircraftsInHangar.length + ', Ammo storeage: ' + this.ammoStorage + ', Total Damage: ' + totalDamage + ', Health Remaining: ' + this.healthRemaining);
  }
};

Carrier.prototype.fill = function(){
  if (this.ammoStorage <= 0) {
    console.log('Error: not enough ammo to refill!');
  } else {
    this.aircraftsInHangar.forEach(function(aircraft){
        this.ammoStorage = aircraft.refill(this.ammoStorage);
    }, this);
  }
};

Carrier.prototype.fight = function(){
  let totalDamage = 0;
  this.aircraftsInHangar.forEach(function(aircraft){
    totalDamage += aircraft.fight();
  });
  return totalDamage;
};


var newAircraft_1 = new Aircraft('F16');
var newAircraft_2 = new Aircraft('F35');
var newAircraft_3 = new Aircraft('F16');
var newAircraft_4 = new Aircraft('F35');


var newCarrier = new Carrier();
newCarrier.add_aircraft(newAircraft_1);
newCarrier.add_aircraft(newAircraft_2);
newCarrier.add_aircraft(newAircraft_3);
newCarrier.add_aircraft(newAircraft_4);

newCarrier.status_report();
newCarrier.fill();
newCarrier.status_report();
newCarrier.fight();
newCarrier.status_report();
newCarrier.fill();
newCarrier.status_report();
