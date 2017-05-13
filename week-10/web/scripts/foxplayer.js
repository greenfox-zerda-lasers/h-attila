// **********************
// P5 FOR SOUND ANIMATION
// **********************

// P5 player is demo only, it use a different player

let sound;

function preload() {
  sound = loadSound('music/Organoid_-_09_-_Purple_Drift.mp3');
}

function setup() {
  let cnv = createCanvas(600, 250);
  cnv.parent('myContainer');
  cnv.mouseClicked(togglePlay);
  fft = new p5.FFT();
}

function draw() {
  background(200);

  let waveform = fft.waveform();
  noFill();
  beginShape();
  stroke(255, 0, 0); // waveform is red
  strokeWeight(1);
  for (let i = 0; i < waveform.length; i++) {
    var x = map(i, 0, waveform.length, 0, width);
    var y = map(waveform[i], -1, 1, 0, height);
    vertex(x, y);
  }
  endShape();

  text('click to play/pause', 4, 10);
}

// fade sound if mouse is over canvas
function togglePlay() {
  if (sound.isPlaying()) {
    sound.pause();
  } else {
    sound.loop();
  }
}


// ***********************
//  SERVER COMMUNICATION
// ***********************

var ajax = {

  // SETTING UP SERVER COMMUNICATION
  talkToServer(method, additionalUrl, data, callbackFunc) {
    var url = `http://localhost:3000${additionalUrl}`;
    var httpRequest = new XMLHttpRequest();
    httpRequest.open(method, url, true);
    httpRequest.setRequestHeader('Content-Type', 'application/json; charset=utf-8');

    // IF data EXIST
    (data) ? httpRequest.send(JSON.stringify(data)) : httpRequest.send();

    httpRequest.onreadystatechange = () => {
      if (httpRequest.readyState === XMLHttpRequest.DONE) {
        callbackFunc(JSON.parse(httpRequest.response));
      }
    };
  },
};


// **********************
// MAIN APP DEFINITIONS
// **********************

var app = {

  // CURRENT PLAYED TRACK
  actualTrackID: 0,
  actualPlayListID: 1,

  // CURRENT TRACKLIST
  playTracks: [],

  // AUDIO DATA
  audioPlayer: document.querySelector('audio'),

  // app STARTS, GET INIT DATA
  init: () => {
    ajax.talkToServer('GET', '/playlists', null, app.playlistsCreate);
    ajax.talkToServer('GET', '/playlis-tracks/', null, app.trackListCreate);
  },

  // LOGO, NOTIFICATIONS
  logo: function () {
    // logo, notifications comes here
  },

  // CREATE, LIST PLAYLISTS ON LEFT PANEL
  playlistsCreate: function (playList) {
    var playLists = document.querySelector('.left-playlist');
    playLists.innerHTML = '';

    // CREATE PLAYLISTS
    playList.forEach((item, index) => {
      var playlistItem = document.createElement('div');
      var playlistName = document.createElement('p');
      var playlistItemDelete = document.createElement('p');

      playlistItem.className = 'playlist-item';
      playlistName.className = 'playlist-name';
      playlistName.id = item.id;
      playlistName.innerHTML = item.playlistName;
      playlistItem.appendChild(playlistName);

      // 'All TRACKS' AND 'FAVORITES' CAN NOT DELETE
      if (index >= 2) {
        playlistItemDelete.className = 'playlist-delete';
        playlistItemDelete.id = item.id;
        playlistItem.appendChild(playlistItemDelete);

        // DELETE PLAYLIST BY ID - EVENT LISTENER
        playlistItemDelete.addEventListener('click', () => {
          ajax.talkToServer('DELETE', '/playlists/' + playlistItemDelete.id, null, app.playlistsCreate);
        });
      }

        // LIST THE TRACKS OF THE PLAYLIST - EVENT LISTENER
      playlistName.addEventListener('click', () => {
        app.actualPlayListID = playlistName.id;
        ajax.talkToServer('GET', '/playlis-tracks/' + app.actualPlayListID, null, app.trackListCreate);
      });
      playLists.appendChild(playlistItem);
    });
  },

  // LIST TRACKS ON RIGHT PANEL
  trackListCreate: (playTracks) => {
    app.playTracks = playTracks;
    var trackItems = document.querySelector('.right-songs');
    trackItems.innerHTML = '';
    playTracks.forEach((track, index) => {
      var newTrack = document.createElement('div');
      var trackId = document.createElement('p');
      var trackTitle = document.createElement('p');
      var trackLength = document.createElement('p');

      newTrack.className = 'track-item';
      newTrack.id = track.id;
      trackId.className = 'track-id';
      trackTitle.className = 'track-title';
      trackLength.className = 'track-length';

      trackId.innerHTML = index + 1;
      trackTitle.innerHTML = track.title;
      trackLength.innerHTML = track.length;

      newTrack.appendChild(trackId);
      newTrack.appendChild(trackTitle);
      newTrack.appendChild(trackLength);
      newTrack.addEventListener('click', () => {
        app.actualTrackID = track.id;
        app.audioPlayer.setAttribute('src', app.playTracks[index].path);
        actualSongTitle.innerHTML = app.playTracks[index].title;
        actualSongAuthor.innerHTML = app.playTracks[index].author;
        var actualSongCover = document.querySelector('.left-cover');
        if (app.playTracks[index].cover !== '') {
          actualSongCover.style.backgroundImage = 'url(' + app.playTracks[index].cover + ')';
        } else {
          actualSongCover.style.backgroundImage = 'url("../images/music-placeholder.png")';
        }
      });
      trackItems.appendChild(newTrack);
    });
  },
};


// *****************
//  EVENT HANDLING
// *****************

// ADD NEW PLAYLIST - OPENS POPUP WINDOW
var addNewPlaylist = document.querySelector('.add-new-playlist');
addNewPlaylist.addEventListener('click', () => {
  // CREATE NEW PLAYLIST - DIALOG BOX
  vex.dialog.prompt({
    message: 'Please add the new list name',
    placeholder: 'newlist',
    callback: (value) => {
      ajax.talkToServer('POST', '/playlists', { value }, app.playlistsCreate);
    },
  });
});

// ADD NEW TRACK TO THE PLAYLIST
// this function under construction - missing selector in dialog box
//
// let addToPlaylist = document.querySelector('.add-to-playlist');
//
// SELECT PLAYLIST - DIALOG BOX
// vex.dialog.prompt({
//   message: 'Please select the playlist',
//   placeholder: 'newlist',
//   callback: (value) => {
//     ajax.talkToServer('POST', '/playlists', { value }, app.playlistsCreate);
//   },
// });
// addToPlaylist.addEventListener('click', () => {
//   ajax.talkToServer('POST', '/playlist-tracks/' + app.actualPlayListID + '/', app.playTracks[app.actualTrackID].id, null, app.trackListCreate);
// });

// ADD NEW TRACK TO THE FAVORITES
var addToFavorites = document.querySelector('.add-to-favorites');
addToFavorites.addEventListener('click', () => {
  ajax.talkToServer('POST', '/playlist-tracks/2/' + app.actualTrackID, null, app.trackListCreate);
});


// **************************
// AUDIO PLAYER TIME EVENTS
// **************************

var audioCurrentTime = document.querySelector('.current-time');
var totalLength = document.querySelector('.total-length');

// SEEK BAR FOR MEDIA PLAY
// Initialize a new plugin instance for element or array of elements.
var slider = document.querySelector('.range-seek');
rangeSlider.create(slider, {
  polyfill: true,     // Boolean, if true, custom markup will be created
  rangeClass: 'rangeSlider',
  disabledClass: 'rangeSlider--disabled',
  fillClass: 'rangeSlider__fill',
  bufferClass: 'rangeSlider__buffer',
  handleClass: 'rangeSlider__handle',
  startEvent: ['mousedown', 'touchstart', 'pointerdown'],
  moveEvent: ['mousemove', 'touchmove', 'pointermove'],
  endEvent: ['mouseup', 'touchend', 'pointerup'],
  min: null,          // Number , 0
  max: null,          // Number, 100
  step: null,         // Number, 1
  value: null,        // Number, center of slider
  buffer: null,       // Number, in percent, 0 by default
  stick: null,        // [Number stickTo, Number stickRadius] : use it if
                      // handle should stick to stickTo-th value in stickRadius
  borderRadius: 10,   // Number, if you use buffer + border-radius in css for looks good,

  onSlide: (position, value) => {
    seek(value);
  },
});

// TIME CHANGE EVENTS, REFRESH ACTUAL TRACK POSITION, DURATION, SLIDER
app.audioPlayer.addEventListener('timeupdate', () => {
  var timeSecFromMillisec = (seconds) => {
    sec = Math.floor(seconds);
    min = Math.floor(sec / 60);
    min = min >= 10 ? min : '0' + min;
    sec = Math.floor(sec % 60);
    sec = sec >= 10 ? sec : '0' + sec;
    return min + ':' + sec;
  };

  if (!isNaN(app.audioPlayer.duration)) {
    audioCurrentTime.innerHTML = '<p>' + timeSecFromMillisec(app.audioPlayer.currentTime) + '</p>';
    totalLength.innerHTML = '<p>' + timeSecFromMillisec(app.audioPlayer.duration) + '</p>';

    if (app.audioPlayer.duration === app.audioPlayer.currentTime && app.actualTrackID < app.playTracks.length - 1) {
      loadNextTrack();
    }
    slider.rangeSlider.update({ value: app.audioPlayer.currentTime / app.audioPlayer.duration * 100 });
  }
}, false);


// *********************
// AUDIO PLAYER EVENTS
// *********************

// REFRESH SEEK SLIDER
function seek(percent) {
  app.audioPlayer.currentTime = app.audioPlayer.duration * percent;
}

// PREVIOUS SONG
var prevSong = document.querySelector('.prev');
prevSong.addEventListener('click', () => {
  if (app.actualTrackID > 0) {
    app.actualTrackID -= 1;
  }
  app.audioPlayer.setAttribute('src', app.playTracks[app.actualTrackID].path);
  actualSongTitle.innerHTML = app.playTracks[app.actualTrackID].title;
  actualSongAuthor.innerHTML = app.playTracks[app.actualTrackID].author;
  var actualSongCover = document.querySelector('.left-cover');
  if (app.playTracks[app.actualTrackID].cover !== '') {
    actualSongCover.style.backgroundImage = 'url(' + app.playTracks[app.actualTrackID].cover + ')';
  } else {
    actualSongCover.style.backgroundImage = 'url("../images/music-placeholder.png")';
  }
});

// PAUSE SONG
var pauseSong = document.querySelector('.pause');
pauseSong.addEventListener('click', () => {
  if (app.audioPlayer.paused) {
    app.audioPlayer.play();
    pauseSong.style.backgroundImage = 'url(images/pause.svg)';
  } else {
    app.audioPlayer.pause();
    pauseSong.style.backgroundImage = 'url(images/play.svg)';
  }
});

var loadNextTrack = () => {
  if (app.actualTrackID < app.playTracks.length - 1) {
    app.actualTrackID += 1;
  }
  app.audioPlayer.setAttribute('src', app.playTracks[app.actualTrackID].path);
  actualSongTitle.innerHTML = app.playTracks[app.actualTrackID].title;
  actualSongAuthor.innerHTML = app.playTracks[app.actualTrackID].author;
  var actualSongCover = document.querySelector('.left-cover');
  if (app.playTracks[app.actualTrackID].author !== '') {
    actualSongCover.style.backgroundImage = 'url(' + app.playTracks[app.actualTrackID].cover + ')';
  } else {
    actualSongCover.style.backgroundImage = 'url("../images/music-placeholder.png")';
  }
};

// NEXT SONG
var nextSong = document.querySelector('.next');
nextSong.addEventListener('click', () => {
  loadNextTrack();
});

// SHUFFLE SONG
var shuffleSong = document.querySelector('.shuffle');
shuffleSong.addEventListener('click', () => {
  console.log('shuffle song');
});

// MUTE SONG
var muteSong = document.querySelector('.mute');
muteSong.addEventListener('click', () => {
  console.log('mute song');
});


var actualSongTitle = document.querySelector('h2');
var actualSongAuthor = document.querySelector('h3');

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
  max: 100,        // Number, 100
  step: 1,         // Number, 1
  value: 100,      // Number, center of slider
  buffer: 0,       // Number, in percent, 0 by default
  stick: 0,        // [Number stickTo, Number stickRadius] : use it if handle
                   // should stick to stickTo-th value in stickRadius
  borderRadius: 1, // Number, if you use buffer + border-radius in css for looks good,

  onSlide: function (position, value) {
    app.audioPlayer.volume = value;
    if (value === 0) {
      muteSong.style.backgroundImage = 'url(images/mute_new.svg)';
      muteSong.style.backgroundSize = '20px';
      this.value = 100;
    } else {
      muteSong.style.backgroundImage = 'url(images/volume.svg)';
      muteSong.style.backgroundSize = '10px';
    }
  },
});


// THUMBNAIL ANIMATION
var thumbnailsButton = document.querySelector('.panel-button');
var thumbnailsPanel = document.querySelector('#thumbnails');
thumbnailsButton.addEventListener('click', () => {
  thumbnailsPanel.classList.toggle('panel-close');
  if (thumbnailsPanel.classList.contains('panel-close')) {
    thumbnailsButton.style.transform = 'rotate(180deg)';
  } else {
    thumbnailsButton.style.transform = 'rotate(0deg)';
  }
});

// ****************************
//  MAIN PROGRAM STARTS HERE
// ****************************

app.init();
