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
  title : "Never Give Up",
  path : "music/Ars_Sonor_-_02_-_Never_Give_Up.mp3",
  author : "Ars Sonor",
  length : "1:20",
  playlist_id: [1],
},
{
  id : 2,
  title : "Doctor Talos Answers The Door",
  path : "music/Doctor_Turtle_-_Doctor_Talos_Answers_The_Door.mp3",
  author : "Doctor Turtle",
  length : "2:10",
  playlist_id: [1],
},
{
  id : 3,
  title : "Purple Drift",
  path : "music/Organoid_-_09_-_Purple_Drift.mp3",
  author : "Organoid",
  length : "3:30",
  playlist_id: [1],
}];

// PLAYLISTS DATA
var playlists = [
{
  id: 1,
  playlistName: "All tracks",
  system: "wtf",
},
{
  id: 2,
  playlistName: "Favorites",
},
{
  id: 3,
  playlistName: "1 playlist",
},
{
  id: 4,
  playlistName: "2 playlist",
},
];

// GET PLAYLISTS FROM SERVER ** api ok
app.get('/playlists', function (req, res) {
  res.json(playlists);
});

// POST NEW PLAYLIST TO THE SERVER - ADD NEW PLAYLIST
app.post('/playlists', function (req, res) {
  console.log(req.body);
  var newId = playlists[playlists.length-1].id + 1;
  var newPlaylistItem = { "id": newId, "playlistName": req.body.value};
  playlists.push(newPlaylistItem);
  res.json(playlists);
});

// DELETE PLAYLIST BY ID ** api ok
app.delete('/playlists/:id', function (req, res) {
  playlists.forEach (function (playlistItem, index) {
    if (playlistItem.id === parseInt(req.params.id)) {
      playlists.splice(index, 1);
    }
  });
  res.json(playlists);
});

// GET ALL TRACKS ** api ok
app.get('/playlis-tracks/', function (req, res) {
  res.json(tracks);
});

// LIST THE TRACKS OF THE PLAYLIST
app.get('/playlis-tracks/:playlist_id', function (req, res) {
  var playlists = tracks.filter( function (item) {
    return item.playlist_id === parseInt(req.params.playlist_id);
  });
  res.json(playlists);
});

// ADD NEW TRACK TO THE PLAYLIST BY ID
app.post('/playlist-tracks/:playlist_id/:track_id', function (req, res) {
  tracks.forEach (function (trackItem, index) {
    if (trackItem.id === parseInt(req.params.track_id)) {
      if (trackItem.playlist_id.each(function(){
      //   return
      }));
      trackItem.playlist_id = parseInt(req.params.playlist_id);
      console.log(trackItem, req.params.playlist_id);
    }
  });
  res.json(tracks);
});

// DELETE THE TRACK FROM THE PLAYLIST
app.delete('/playlist-tracks/:playlist_id/:track_id', function (req, res) {
  tracks.forEach (function (trackItem, index) {
    if (trackItem.id === parseInt(req.params.track_id)) {
      trackItem.playlist_id = 1;
    }
  });
  res.send(tracks);
});

// START SERVER
var port = process.env.PORT || 3000;

app.listen(port, function () {
  console.log('Server running on port %d', port);
});
