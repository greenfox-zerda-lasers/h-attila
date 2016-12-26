// require('image_data.js')

var numberOfImages = 7;
var imageData = [];
var imagesArr = [];
var currentImagePos = 0;

// CREATING IMAGES DATA TO imagesArr
for (var i=0; i<numberOfImages; i++){
  imageData.push('nature_' + i + '.jpg');
  imageData.push('nature_' + i + '_thumb.jpg');
  imagesArr.push(imageData);
  imageData = [];
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
  if (currentImagePos>=imagesArr.length-1){
    currentImagePos=imagesArr.length-1;
  }
  mainImageChanger(currentImagePos);
});

// UPDATE MAIN IMAGE
function mainImageChanger(currentImagePos){
  var imageBody = document.querySelector('.main-image-box');
  imageBody.style.backgroundImage = 'url("images/' + imagesArr[currentImagePos][0] + '")';
};

// THUMBNAILS
var thumbnailsContainer = document.querySelector('.thumbnails-container');
for (var i=0; i<imagesArr.length; i++){
  var newThumbnail = document.createElement('div');
  newThumbnail.className = 'thumbnail';
  newThumbnail.id = i;
  newThumbnail.style.backgroundImage = 'url("images/' + imagesArr[i][1] + '")';
  newThumbnail.addEventListener('click', function(){
    mainImageChanger(this.id);
  });
  thumbnailsContainer.appendChild(newThumbnail);
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
  };
});
