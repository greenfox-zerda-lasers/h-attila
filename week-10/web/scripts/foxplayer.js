// AUDIO DATA

var actualTrackID = 0;

var audioPlayer = document.querySelector('audio');
console.log(audioPlayer.src);

var playList = [{
  id : 1,
  name : 'Relaxing music for programming',
  tracks : [],
},
{
  id : 2,
  name : 'Party',
  tracks : [],
}];

var playTracks = [
{
  id : 1,
  title : 'Never Give Up',
  file : 'music/Ars_Sonor_-_02_-_Never_Give_Up.mp3',
  author : 'Ars Sonor',
  length : '1:20',
},
{
  id : 2,
  title : 'Doctor Talos Answers The Door',
  file : 'music/Doctor_Turtle_-_Doctor_Talos_Answers_The_Door.mp3',
  author : 'Doctor Turtle',
  length : '2:10',
},
{
  id : 3,
  title : 'Purple Drift',
  file : 'music/Organoid_-_09_-_Purple_Drift.mp3',
  author : 'Organoid',
  length : '3:30',
}];

// LIST PLAYLISTS ON LEFT PANEL
var playLists = document.querySelector('.left-playlist');
playList.forEach (function(playlist, index) {
  var playlistItem = document.createElement('div');
  var playlistName = document.createElement('p');
  var playlistDelete = document.createElement('p');

  playlistItem.className = 'playlist-item';
  playlistName.className = 'playlist-name';
  playlistDelete.className = 'playlist-delete';
  playlistName.innerHTML = playlist.name;

  playlistItem.appendChild(playlistName);
  playlistItem.appendChild(playlistDelete);
  playLists.appendChild(playlistItem);
});

// LIST TRACKS ON RIGHT PANEL
var tracks = document.querySelector('.right-songs');
playTracks.forEach (function(track, index) {
  var newTrack = document.createElement('div');
  var trackId = document.createElement('p');
  var trackTitle = document.createElement('p');
  var trackLength = document.createElement('p');

  newTrack.className = 'track-item';
  trackId.className = 'track-id';
  trackTitle.className = 'track-title';
  trackLength.className = 'track-length';

  trackId.innerHTML = index + 1;
  trackTitle.innerHTML = track.title;
  trackLength.innerHTML = track.length;

  newTrack.appendChild(trackId);
  newTrack.appendChild(trackTitle);
  newTrack.appendChild(trackLength);
  tracks.appendChild(newTrack);
});

// EVENT HANDLING
var addNewPlaylist = document.querySelector('.add-new-playlist');
addNewPlaylist.addEventListener('click', function(){
  console.log('add new playlist');
});

var addToPlaylist = document.querySelector('.add-to-playlist');
addToPlaylist.addEventListener('click', function(){
  console.log('add sont to playlist');
});

var addToFavorites = document.querySelector('.add-to-favorites');
addToFavorites.addEventListener('click', function(){
  console.log('add song to favorites');
});

var prevSong = document.querySelector('.prev');
prevSong.addEventListener('click', function(){
  actualTrackID -= 1;
  audioPlayer.setAttribute('src', playTracks[actualTrackID].file);
  actualSongTitle.innerHTML = playTracks[actualTrackID].title
  actualSongAuthor.innerHTML = playTracks[actualTrackID].author
  console.log(playTracks[actualTrackID].file);
});

var pauseSong = document.querySelector('.pause');
pauseSong.addEventListener('click', function(){
  if (audioPlayer.paused) {
    console.log(audioPlayer.duration);
    audioPlayer.play();
    pauseSong.style.backgroundImage = "url(images/pause.svg)"
  } else {
    console.log(audioPlayer.duration);
    audioPlayer.pause();
    pauseSong.style.backgroundImage = "url(images/play.svg)"
  }
});

var nextSong = document.querySelector('.next');
nextSong.addEventListener('click', function(){
  actualTrackID += 1;
  audioPlayer.setAttribute('src', playTracks[actualTrackID].file);
  actualSongTitle.innerHTML = playTracks[actualTrackID].title
  actualSongAuthor.innerHTML = playTracks[actualTrackID].author
  console.log(playTracks[actualTrackID].file);
});

var shuffleSong = document.querySelector('.shuffle');
shuffleSong.addEventListener('click', function(){
  console.log('shuffle song');
});

var muteSong = document.querySelector('.mute');
muteSong.addEventListener('click', function(){
  console.log('mute song');
});

var actualSongTitle = document.querySelector('h2');

var actualSongAuthor = document.querySelector('h3');


// SEEK BAR FOR MEDIA PLAY
// Initialize a new plugin instance for element or array of elements.
var sliderSeek = document.querySelectorAll('input[type="range-seek"]');
rangeSlider.create(sliderSeek, {
    polyfill: true,     // Boolean, if true, custom markup will be created
    rangeClass: 'rangeSlider',
    disabledClass: 'rangeSlider--disabled',
    fillClass: 'rangeSlider__fill',
    bufferClass: 'rangeSlider__buffer',
    handleClass: 'rangeSlider__handle',
    startEvent: ['mousedown', 'touchstart', 'pointerdown'],
    moveEvent: ['mousemove', 'touchmove', 'pointermove'],
    endEvent: ['mouseup', 'touchend', 'pointerup'],
    min: 0,          // Number , 0
    max: 100,          // Number, 100
    step: 1,         // Number, 1
    value: 0,        // Number, center of slider
    buffer: 0,       // Number, in percent, 0 by default
    stick: 0,        // [Number stickTo, Number stickRadius] : use it if handle should stick to stickTo-th value in stickRadius
    borderRadius: 1,    // Number, if you use buffer + border-radius in css for looks good,
    //onInit: function () {
    //    console.info('onInit');
    // },
    //onSlideStart: function (position, value) {
    //    console.info('onSlideStart', 'position: ' + position, 'value: ' + value);
    // },
    onSlide: function (position, value) {
        console.log('onSlide', 'position: ' + position, 'value: ' + value);
    },
    //onSlideEnd: function (position, value) {
    //    console.warn('onSlideEnd', 'position: ' + position, 'value: ' + value);
    //}
});

var sliderVolume = document.querySelectorAll('input[type="range-volume"]');
rangeSlider.create(sliderVolume, {
    polyfill: true,     // Boolean, if true, custom markup will be created
    rangeClass: 'rangeSlider',
    disabledClass: 'rangeSlider--disabled',
    fillClass: 'rangeSlider__fill',
    bufferClass: 'rangeSlider__buffer',
    handleClass: 'rangeSlider__handle',
    startEvent: ['mousedown', 'touchstart', 'pointerdown'],
    moveEvent: ['mousemove', 'touchmove', 'pointermove'],
    endEvent: ['mouseup', 'touchend', 'pointerup'],
    min: 0,          // Number , 0
    max: 100,          // Number, 100
    step: 1,         // Number, 1
    value: 0,        // Number, center of slider
    buffer: 0,       // Number, in percent, 0 by default
    stick: 0,        // [Number stickTo, Number stickRadius] : use it if handle should stick to stickTo-th value in stickRadius
    borderRadius: 1,    // Number, if you use buffer + border-radius in css for looks good,
    //onInit: function () {
    //    console.info('onInit');
    // },
    //onSlideStart: function (position, value) {
    //    console.info('onSlideStart', 'position: ' + position, 'value: ' + value);
    // },
    onSlide: function (position, value) {
        console.log('onSlide', 'position: ' + position, 'value: ' + value);
        audioPlayer.volume = value;
        if (value === 0){
          muteSong.style.backgroundImage = "url(images/mute_new.svg)";
          muteSong.style.backgroundSize = '20px';
        } else {
          muteSong.style.backgroundImage = "url(images/volume.svg)";
          muteSong.style.backgroundSize = '10px';
        }
    },
    //onSlideEnd: function (position, value) {
    //    console.warn('onSlideEnd', 'position: ' + position, 'value: ' + value);
    //}
});

// USE SEEK BAR FOR PLAY SONG
//var giveMeSomeEvents = true; // or false
//slider.rangeSlider.update({min : 0, max : 20, step : 0.5, value : 1.5, buffer : 70}, giveMeSomeEvents);
// or
//slider.rangeSlider.onSlideStart = function (position, value) {
//                           console.error('anotherCallback', 'position: ' + position, 'value: ' + value);
//                       };
