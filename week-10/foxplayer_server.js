var server = require('express');
var bodyParser = require('body-parser');

var app = server();
app.use(bodyParser.json());

// INIT STATIC CONTENT
app.use('/', server.static('web'));

// TRACKS DATA
var tracks = [
{ id: 1, title: 'Never Give Up', path: 'music/Ars_Sonor_-_02_-_Never_Give_Up.mp3', length: '2:15', author: 'Ars Sonor', cover: '../covers/ars_sonor_never.png', playlist_id: [1, 3] },
{ id: 2, title: 'Doctor Talos Answers The Door', path: 'music/Doctor_Turtle_-_Doctor_Talos_Answers_The_Door.mp3', length: '2:55', author: 'Doctor Turtle', cover: '../covers/doctor_talos.jpg', playlist_id: [1] },
{ id: 3, title: 'Purple Drift', path: 'music/Organoid_-_09_-_Purple_Drift.mp3', length: '3:28', author: 'Organoid', cover: '../covers/organoid.jpg', playlist_id: [1, 4] },
{ id: 4, title: 'Cyanide Sisters', path: 'music/Com_Truise_-_Cyanide_Sisters.mp3', length: '1:56', author: 'Com Truise', cover: '../covers/tom_cruse.jpg', playlist_id: [1, 4] },
{ id: 5, title: 'Slow Peels', path: 'music/Com_Truise_-_Slow_Peels.mp3', length: '4:41', author: 'Com Truise', cover: '../covers/tom_cruse.jpg', playlist_id: [1, 4] },
{ id: 6, title: 'Beware', path: 'music/Death_Grips_-_Beware.mp3', length: '5:53', author: 'Death Gips', cover: '../covers/Dead_Gipsy_Exmilitary.png', playlist_id: [1, 5] },
{ id: 7, title: 'Guillotine', path: 'music/Death_Grips_-_Guillotine.mp3', length: '3:44', author: 'Death Gips', cover: '../covers/Dead_Gipsy_Exmilitary.png', playlist_id: [1, 5] },
{ id: 8, title: 'Takyon (Death Yon)', path: 'music/Death_Grips_-_Takyon_Death_Yon.mp3', length: '2:48', author: 'Death Gips', cover: '../covers/Dead_Gipsy_Exmilitary.png', playlist_id: [1, 5] },
{ id: 9, title: 'Your First Light My Eventide', path: 'music/The_Echelon_Effect_-_Your_First_Light_My_Eventide.mp3', length: '5:10', author: 'The Echelon Effect', cover: '../covers/The_Echelon_Effect.jpg', playlist_id: [1] },
{ id: 10, title: 'Contrails', path: 'music/Glowworm_-_Contrails.mp3', length: '4:41', author: 'Glowworm', cover: '../covers/glowworm.jpg', playlist_id: [1, 6] },
{ id: 11, title: 'Periphescence', path: 'music/Glowworm_-_Periphescence.mp3', length: '3:59', author: 'Glowworm', cover: '../covers/glowworm.jpg', playlist_id: [1, 6] },
{ id: 12, title: 'Ghost', path: 'music/Motorama_-_Ghost.mp3', length: '3:48', author: 'Motorama', cover: '../covers/alps.jpg', playlist_id: [1, 7] },
{ id: 13, title: 'Normandy', path: 'music/Motorama_-_Normandy.mp3', length: '3:37', author: 'Motorama', cover: '../covers/alps.jpg', playlist_id: [1, 7] },
{ id: 14, title: 'Anchor', path: 'music/Motorama_-_Anchor.mp3', length: '3:17', author: 'Motorama', cover: '../covers/alps.jpg', playlist_id: [1, 7] },
{ id: 15, title: 'You', path: 'music/Nils_Frahm_-_You.mp3', length: '3:09', author: 'Nils Frahm', cover: '../covers/screws.jpg', playlist_id: [1] },
];

// PLAYLISTS DATA
var playlists = [
  { id: 1, playlistName: 'All tracks' },
  { id: 2, playlistName: 'Favorites' },
  { id: 3, playlistName: 'Ars Sonor' },
  { id: 4, playlistName: 'Com Truise' },
  { id: 5, playlistName: 'Death Gips' },
  { id: 6, playlistName: 'Glowworm' },
  { id: 7, playlistName: 'Motorama' },
];

// GET PLAYLISTS FROM SERVER
app.get('/playlists', function (req, res) {
  res.json(playlists);
});

// POST NEW PLAYLIST TO THE SERVER - ADD NEW PLAYLIST
app.post('/playlists', function (req, res) {
  var newId = playlists[playlists.length - 1].id + 1;
  var newPlaylistItem = { id: newId, playlistName: req.body.value };
  playlists.push(newPlaylistItem);
  res.json(playlists);
});

// DELETE PLAYLIST BY ID
app.delete('/playlists/:id', function (req, res) {
  playlists.forEach(function (playlistItem, index) {
    if (playlistItem.id === parseInt(req.params.id, 10)) {
      playlists.splice(index, 1);
    }
  });
  res.json(playlists);
});

// GET ALL TRACKS
app.get('/playlis-tracks/', function (req, res) {
  res.json(tracks);
});

// LIST THE TRACKS OF THE PLAYLIST
app.get('/playlis-tracks/:playlist_id', function (req, res) {
  playlists = tracks.filter(function (trackItem) {
    return trackItem.playlist_id.indexOf(parseInt(req.params.playlist_id, 10)) >= 0;
  });
  res.json(playlists);
});

// ADD NEW TRACK TO THE PLAYLIST BY ID
app.post('/playlist-tracks/:playlist_id/:track_id', function (req, res) {
  tracks.forEach(function (trackItem) {
    if (trackItem.id === parseInt(req.params.track_id, 10)) {
      if (trackItem.playlist_id.indexOf(req.params.track_id) < 0) {
        trackItem.playlist_id.push(parseInt(req.params.playlist_id, 10));
      }
    }
  });
  res.json(tracks);
});

// DELETE THE TRACK FROM THE PLAYLIST
app.delete('/playlist-tracks/:playlist_id/:track_id', function (req, res) {
  tracks.forEach(function (trackItem) {
    if (trackItem.id === parseInt(req.params.track_id, 10)) {
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
