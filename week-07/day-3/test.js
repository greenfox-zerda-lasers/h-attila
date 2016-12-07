function Car(startKm) {
  this.km = startKm;
  this.ride = function(km) {
    this.km += km;
  }
}

var car = new Car(120000);

car.ride(200);
console.log(car.km); // 120200
