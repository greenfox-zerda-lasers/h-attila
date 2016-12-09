var imageList = [
[ "url('images/nature_0.jpg')", '<p>1. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do ut labore et dolore magna aliqua.</p>' ],
[ "url('images/nature_1.jpg')", '<p>2. Ut enim ad minim veniam, quis nostrud exercitation.</p>' ],
[ "url('images/nature_2.jpg')", '<p>3. Ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute in voluptate velit esse cillum.</p>' ],
[ "url('images/nature_3.jpg')", '<p>4. Dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non.</p>' ],
[ "url('images/nature_4.jpg')", '<p>5. Toident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>' ],
[ "url('images/nature_5.jpg')", '<p>6. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque.</p>' ],
[ "url('images/nature_6.jpg')", '<p>7. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni.</p>' ],
[ "url('images/nature_7.jpg')", '<p>8. Ut enim ad minima veniam, quis nostrum suscipit laboriosam, nisi ut aliquid ex ea commodi.</p>' ]
];

var imageListForThumb = [
  "url('images/nature_0_thumb.jpg')",
  "url('images/nature_1_thumb.jpg')",
  "url('images/nature_2_thumb.jpg')",
  "url('images/nature_3_thumb.jpg')",
  "url('images/nature_4_thumb.jpg')",
  "url('images/nature_5_thumb.jpg')",
  "url('images/nature_6_thumb.jpg')",
  "url('images/nature_7_thumb.jpg')"
];

var imgCurrentPosition = 0;

var thumbnailImages = document.querySelectorAll(".thumb");
for (i=0; i<thumbnailImages.length; i++){
  thumbnailImages[i].style.backgroundImage = imageListForThumb[i];
}

var leftButtonClick = document.querySelector('.left');
var rightButtonClick = document.querySelector('.right');

function onRightButtonClick(){
  if (imgCurrentPosition < imageList.length-1){
    imgCurrentPosition++;
  }
  setNewImage(imgCurrentPosition);
}

function onLeftButtonClick(){
  if (imgCurrentPosition > 0){
    imgCurrentPosition--;
  }
  setNewImage(imgCurrentPosition);
}

var imageContainer = document.querySelector('#thumbnails');
imageContainer.addEventListener('click', thumbNavigate);

function thumbNavigate(event){
  setNewImage(event.target.id-1);
}

function setNewImage(position){
  document.querySelector('.main-picture').style.backgroundImage = imageList[position][0];
  document.querySelector('.main-picture').innerHTML = imageList[position][1];
}

var thumbnailButton = document.querySelector('.button');
thumbnailButton.addEventListener('click', function(){
  if (imageContainer.className == 'close'){
    imageContainer.className = '';
    thumbnailButton.style.transform = 'rotate(0deg)';
  } else {
    imageContainer.className = 'close';
    thumbnailButton.style.transform = 'rotate(180deg)';
  }
});

leftButtonClick.addEventListener('click', onLeftButtonClick);
rightButtonClick.addEventListener('click', onRightButtonClick);