let httpRequest = new XMLHttpRequest();
httpRequest.open('GET', 'http://api.giphy.com/v1/gifs/search?q=funny+cat&limit=16&api_key=dc6zaTOxFJmzC', true); // Also try http://444.hu/feed
httpRequest.send(null);

arrayOfImages = [];

httpRequest.onreadystatechange = function(){
  if (httpRequest.readyState === XMLHttpRequest.DONE){
    var resp = JSON.parse(httpRequest.response);
    console.log(resp.data);

    resp.data.forEach(function(item){
      var newAnimatedImage = document.createElement('img');
      newAnimatedImage.setAttribute('src', item.images.downsized_large.url);
      arrayOfImages.push(newImage);
      document.body.appendChild(newImage);
    });
  }
  console.log(arrayOfImages);
};
