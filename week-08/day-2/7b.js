// Embed the following file to a HTML document:
//  - From the previous flickr example extract the .jpg link directly
//  - Create an image tag in the with document.createElement
//  - Add a 'load' event to the image and only show the image to the user when the image is loaded

var newImage = document.createElement('img');
newImage.src = 'https://c7.staticflickr.com/8/7562/15584243094_342cdf7575_o.jpg';
newImage.addEventListener('load', function(){
  document.body.appendChild(newImage);
});
