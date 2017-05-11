let numberOfImages = 7;
let imageData = [];
let imagesArr = [];
let currentImagePos = 0;

// CREATING IMAGES DATA TO imagesArr
for (let i=0; i<numberOfImages; i++){
  imageData.push('nature_' + i + '.jpg');
  imageData.push('nature_' + i + '_thumb.jpg');
  imagesArr.push(imageData);
  imageData = [];
}

// LEFT-RIGHT BUTTONS
let leftButton = document.querySelector('.left');
leftButton.addEventListener('click', function(){
  currentImagePos--;
  if (currentImagePos<=0){
    currentImagePos=0;
  }
  mainImageChanger(currentImagePos);
});

let rightButton = document.querySelector('.right');
rightButton.addEventListener('click', function(){
  currentImagePos++;
  if (currentImagePos>=imagesArr.length-1){
    currentImagePos=imagesArr.length-1;
  }
  mainImageChanger(currentImagePos);
});

// UPDATE MAIN IMAGE
function mainImageChanger(currentImagePos){
  let imageBody = document.querySelector('.main-image-box');
  imageBody.style.backgroundImage = 'url("images/' + imagesArr[currentImagePos][0] + '")';
};

// THUMBNAILS
let thumbnailsContainer = document.querySelector('.thumbnails-container');
for (let i=0; i<imagesArr.length; i++){
  let newThumbnail = document.createElement('div');
  newThumbnail.className = 'thumbnail';
  newThumbnail.id = i;
  newThumbnail.style.backgroundImage = 'url("images/' + imagesArr[i][1] + '")';
  newThumbnail.addEventListener('click', function(){
    mainImageChanger(this.id);
  });
  thumbnailsContainer.appendChild(newThumbnail);
}

// THUMBNAIL ANIMATION
let thumbnailsButton = document.querySelector('.panel-button');
let thumbnailsPanel = document.querySelector('#thumbnails');
thumbnailsButton.addEventListener('click', function(){
  thumbnailsPanel.classList.toggle('panel-close');
  if (thumbnailsPanel.classList.contains('panel-close')){
    thumbnailsButton.style.transform = 'rotate(180deg)';
  } else {
    thumbnailsButton.style.transform = 'rotate(0deg)';
  };
});
