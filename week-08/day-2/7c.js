// Based on the previous example create an array of images taken from flickr
// https://www.flickr.com/photos/jasontravis/26683911430/in/album-72157603258446753/
// https://www.flickr.com/photos/jasontravis/16635664865/in/album-72157603258446753/
// https://www.flickr.com/photos/jasontravis/14195441260/in/album-72157603258446753/

// Display a progress bar while the images are loading
// You can create your own or use the built in HTML5 version:
// https://developer.mozilla.org/en/docs/Web/HTML/Element/progress

var imgArr = ['https://c7.staticflickr.com/8/7799/26683911430_c4662bf0ec_z.jpg',
          'https://c2.staticflickr.com/9/8574/16635664865_9f5e9e2918_z.jpg',
          'https://c5.staticflickr.com/3/2929/14195441260_7201745aaa_z.jpg'
        ];

var downloadedImage = [];
var downloadedImages = 0;
var progressBar = document.querySelector('.progressbar');

for (var i=0; i<imgArr.length; i++){
  var newImage = document.createElement('img');
  newImage.setAttribute('src', imgArr[i]);
  downloadedImage.push(newImage);
}

downloadedImage[0].addEventListener('load', function(){
  document.body.appendChild(downloadedImage[0]);
  downloadedImages++;
  setProgressBar();
});

downloadedImage[1].addEventListener('load', function(){
  document.body.appendChild(downloadedImage[1]);
  downloadedImages++;
  setProgressBar();
});

downloadedImage[2].addEventListener('load', function(){
  document.body.appendChild(downloadedImage[2]);
  downloadedImages++;
  setProgressBar();
});

function setProgressBar(){
  progressBar.setAttribute('value', Math.round(downloadedImages/3)*100);
}
