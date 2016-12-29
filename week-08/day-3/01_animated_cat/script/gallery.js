var numberOfImages = 7;
var imageData = [];
var imagesArr = [];
var currentImagePos = 0;

// SETTING UP API CONNECTION
var httpRequest = new XMLHttpRequest();
httpRequest.open('GET', 'http://api.giphy.com/v1/gifs/search?q=funny+cat&limit=7&api_key=dc6zaTOxFJmzC', true);
httpRequest.send();

httpRequest.onreadystatechange = function(){
  if (httpRequest.readyState === XMLHttpRequest.DONE){
    var imagesDataFromWeb = JSON.parse(httpRequest.response).data;
    creatingImages(imagesDataFromWeb);
  }
};

// CREATING IMAGES DATA TO imagesArr
function creatingImages(imagesDataFromWeb){
  for (var i=0; i<numberOfImages; i++){
    imageData.push(imagesDataFromWeb[i].images.original.url);
    imageData.push(imagesDataFromWeb[i].images.downsized.url);
    imagesArr.push(imageData);
    imageData = [];
  }

  // CREATING THUMBNAILS
  var thumbnailsContainer = document.querySelector('.thumbnails-container');
  for (var j=0; j<imagesArr.length; j++){
    var newThumbnail = document.createElement('div');
    newThumbnail.className = 'thumbnail';
    newThumbnail.id = j;
    newThumbnail.style.backgroundImage = 'url(' + imagesArr[j][1] + ')';
    newThumbnail.addEventListener('click', function(){
      mainImageChanger(this.id);
    });
    thumbnailsContainer.appendChild(newThumbnail);
  }
}

// LEFT-RIGHT BUTTONS
var leftButton = document.querySelector('.left');
leftButton.addEventListener('click', function(){
  currentImagePos--;
  if (currentImagePos<=0){
    currentImagePos=0;
  }
  mainImageChanger(currentImagePos);
});

var rightButton = document.querySelector('.right');
rightButton.addEventListener('click', function(){
  currentImagePos++;
  if (currentImagePos>=numberOfImages-1){
    currentImagePos=numberOfImages.length-1;
  }
  mainImageChanger(currentImagePos);
});

// UPDATE MAIN IMAGE
function mainImageChanger(currentImagePos){
  var imageBody = document.querySelector('.main-image-box');
  imageBody.style.backgroundImage = 'url(' + imagesArr[currentImagePos][0] + ')';
}

// THUMBNAIL ANIMATION
var thumbnailsButton = document.querySelector('.panel-button');
var thumbnailsPanel = document.querySelector('#thumbnails');
thumbnailsButton.addEventListener('click', function(){
  thumbnailsPanel.classList.toggle('panel-close');
  if (thumbnailsPanel.classList.contains('panel-close')){
    thumbnailsButton.style.transform = 'rotate(180deg)';
  } else {
    thumbnailsButton.style.transform = 'rotate(0deg)';
  }
});
