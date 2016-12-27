// Based on the previous example create an array of images taken from flickr
// https://www.flickr.com/photos/jasontravis/26683911430/in/album-72157603258446753/
// https://www.flickr.com/photos/jasontravis/16635664865/in/album-72157603258446753/
// https://www.flickr.com/photos/jasontravis/14195441260/in/album-72157603258446753/

// Display a progress bar while the images are loading
// You can create your own or use the built in HTML5 version:
// https://developer.mozilla.org/en/docs/Web/HTML/Element/progress

var imgArr = [
  'https://c7.staticflickr.com/8/7799/26683911430_c4662bf0ec_b.jpg',
  'https://c2.staticflickr.com/9/8574/16635664865_9f5e9e2918_b.jpg',
  'https://c5.staticflickr.com/3/2929/14195441260_7201745aaa_b.jpg',
];

var loadedImages = 0;

imgArr.forEach(function(image){
  var newImage = document.createElement('img');
  newImage.src = image;
  newImage.addEventListener('load', function(){
    document.body.appendChild(newImage);
    loadedImages++;
    progressBarUpgrade(loadedImages);
  });
});

function progressBarUpgrade(loadedImages){
  var progressBar = document.querySelector('#progress-bar');
  progressBar.value = Math.round(loadedImages/imgArr.length*100);
}
