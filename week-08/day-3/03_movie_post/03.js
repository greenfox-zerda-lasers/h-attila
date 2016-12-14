var sendButton = document.querySelector('.send-button');
var url = '';
var movietitle = document.querySelector('#movietitle');
var rating = document.querySelector('#rating');
var username = document.querySelector('#username');

sendButton.addEventListener('click', function(){
    var dataToWeb = {
      MovieTitle :  movietitle.value,
      Rating : rating.value,
      Username : username.value
    };
    postToWeb(dataToWeb);
});

function postToWeb(dataToWeb){
  var postingToWeb = XMLHttpRequest;
  postingToWeb.open('POST', url, true);
  postingToWe.send(dataToWeb);
  alert('data posted: ' + dataToWeb.MovieTitle + ', ' + dataToWeb.Rating + ', ' + dataToWeb.Username);
}
