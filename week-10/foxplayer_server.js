var server = require('express');
var bodyParser = require('body-parser');
var app = server();
app.use(bodyParser.json());

// INIT STATIC CONTENT
app.use('/', server.static('web'));


// TRACKS DATA
var tracks = [
{
  id : 1,
  title : 'Never Give Up',
  path : 'music/Ars_Sonor_-_02_-_Never_Give_Up.mp3',
  author : 'Ars Sonor',
  length : '1:20',
  playlist_id: 1,
},
{
  id : 2,
  title : 'Doctor Talos Answers The Door',
  path : 'music/Doctor_Turtle_-_Doctor_Talos_Answers_The_Door.mp3',
  author : 'Doctor Turtle',
  length : '2:10',
  playlist_id: 1,
},
{
  id : 3,
  title : 'Purple Drift',
  path : 'music/Organoid_-_09_-_Purple_Drift.mp3',
  author : 'Organoid',
  length : '3:30',
  playlist_id: 0,
}];

// PLAYLISTS DATA
var playlists = [
{
  id : 1,
  playlistName : 'My first playlist',
  system : 'wtf',
},
{
  id : 2,
  playlistName : 'My second playlist',
  system : 'wtf',
},
{
  id : 3,
  playlistName : 'My 3 playlist',
  system : 'wtf',
},
{
  id : 4,
  playlistName : 'My 4 playlist',
  system : 'wtf',
},
];

// GET PLAYLISTS FROM SERVER
app.get('/playlists', function (req, res) {
  res.send(playlists);
});

// POST NEW PLAYLIST TO THE SERVER
app.post('/playlists', function (req, res) {
  playlists.push(req.body);
  res.send(playlists);
});

// DELETE PLAYLIST BY ID
app.delete('/playlists/:id', function (req, res) {
  playlists.forEach (function (playlistItem, index) {
    if (playlistItem.id === parseInt(req.params.id)) {
      playlists.splice(index, 1);
    }
  });
  res.send(playlists);
});

// GET ALL TRACKS
app.get('/playlis-tracks/', function (req, res) {
  res.json(tracks);
});

// LIST ALL THE TRACKS ADDED TO THE PLAYLIST
app.get('/playlis-tracks/:playlist_id', function (req, res) {
  var responseData = tracks.filter( function (item) {
    return item.playlist_id === parseInt(req.params.playlist_id);
  });
  res.send(responseData);
});

// ADDS THE TRACK TO THE ID'S PLAYLIST
app.post('/playlist-tracks/:playlist_id', function (req, res) {
  tracks.forEach (function (trackItem, index) {
    if (trackItem.id === parseInt(req.params.playlist_id)) {
      trackItem.playlist_id = req.params.playlist_id;
    }
  });
  res.send(tracks);
});

// DELETE THE TRACK FROM THE PLAYLIST
app.delete('/playlist-tracks/:playlist_id/:track_id', function (req, res) {
  tracks.forEach (function (trackItem, index) {
    if (trackItem.id === parseInt(req.params.track_id)) {
      trackItem.playlist_id = 0;
    }
  });
  res.send(tracks);
});

// START SERVER
var port = process.env.PORT || 3000;

app.listen(port, function () {
  console.log('Server running on port %d', port);
});
