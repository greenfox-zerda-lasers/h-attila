// Create a "tour" function that takes two functions as parameters:
//  - walk and distance
//  - distance should return an array of false values [false,false,false] with the length of a given parameter
//  - walk should go through the returned array of distance and change it to true
//  - tour should return the result of walk

var length = 5;

var distance = function(length){
  let result = [];
  for (i =0; i<length; i++){
    result.push(false);
  }
  return result;
};

var walk = function(arr){
  arr.forEach(function(item, index, arr){
    if (item === false){
      arr[index] = true;
    }
  });
  return arr;
};

var tour = function(walk, distance, length){
  console.log(walk(distance(length)));
};

tour(walk, distance, 5);
