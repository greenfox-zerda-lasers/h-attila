// 'use strict';

// create a student object
// that has a method `addgrade`, that takes a grade from 1 to 5
// an other method `getAverage`, that returns the average of the grades

var student = {
  grades : [],
  addgrade : function(grade){
    this.grades.push(grade);
  },
  getaverage : function(){
    var sum = 0;
    this.grades.map(function(item) {
        sum += item;
    });
    return sum / this.grades.length;
  }
};

student.addgrade(1);
student.addgrade(2);
student.addgrade(3);
student.addgrade(4);
student.addgrade(5);

console.log(student.getaverage());
