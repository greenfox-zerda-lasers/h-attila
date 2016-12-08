// 1.
var myImg = document.querySelector('img');
  console.log(myImg.getAttribute('src'));

// 2.
var newImgSrc = "http://rsvpmagazine.ie/wp-content/uploads/2015/08/lLxfU1Kg.jpg";
var myImg = document.querySelector('img');
myImg.setAttribute('src', newImgSrc);

// 3.
var newLink = "http://www.greenfoxacademy.com/";
document.querySelector('a').setAttribute('href', newLink);

// 4.
var button = document.querySelector('.this-one');
button.setAttribute('disabled', 'disabled');
button.innerHTML = 'Do not click me!';
