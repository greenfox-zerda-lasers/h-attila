// Embed the following file to a HTML document:
//  - From the previous flickr example extract the .jpg link directly
//  - Create an image tag in the with document.createElement
//  - Add a 'load' event to the image and only show the image to the user when the image is loaded

var downloadedImage = document.createElement('img');
downloadedImage.src = 'https://c7.staticflickr.com/8/7562/15584243094_2e25d9c978_z.jpg';

downloadedImage.addEventListener('load', function(){
  document.body.appendChild(downloadedImage);
  console.log('image loaded successfully...');
});
