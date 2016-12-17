
// create a student object
// that has a method `addgrade`, that takes a grade from 1 to 5
// an other method `getAverage`, that returns the average of the grades

var Student = function(){
  this.grades = [];
};

Student.prototype.addgrade = function(grade){
    this.grades.push(grade);
};

Student.prototype.getAverage = function(){
  console.log(this.grades.reduce(function(a, b){ return a+b; }, 0) / this.grades.length);
};

var students = new Student();
students.addgrade(3);
students.addgrade(5);
students.getAverage();
