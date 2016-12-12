function Car(km) {
 this.km = km;
}

Car.prototype.ride = function() {
 this.km += 10;
}

var volvo = new Car(0);
volvo.ride(120);
console.log(volvo.km); // 80120
