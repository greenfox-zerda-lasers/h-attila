let httpRequest = new XMLHttpRequest();
httpRequest.open('GET', 'https://api.nytimes.com/svc/search/v2/articlesearch.json?api-key=ecf5a7de7cc04cb2b96621ac0933ae26&q=area+51', true);
httpRequest.send();

var ArrayOfArcticles;

httpRequest.onreadystatechange = function(){
  if (httpRequest.readyState === XMLHttpRequest.DONE){
    var arcticlesObject = JSON.parse(httpRequest.response);
    ArrayOfArcticles = arcticlesObject.response.docs;
    console.log(ArrayOfArcticles);
  }
};

  var arcticleCurrentPosition = 0;

  var leftButtonClick = document.querySelector('.left');
  var rightButtonClick = document.querySelector('.right');
  var arcticleHead = document.querySelector('h1');
  var arcticleSnippet = document.querySelector('.snippet');
  var arcticleDate = document.querySelector('.date');


  function onRightButtonClick(){
    if (arcticleCurrentPosition < ArrayOfArcticles.length-1){
      arcticleCurrentPosition++;
      console.log(arcticleCurrentPosition);

    }
    setNewArcticle(arcticleCurrentPosition);
  }

  function onLeftButtonClick(){
    if (arcticleCurrentPosition > 0){
      arcticleCurrentPosition--;
      console.log(arcticleCurrentPosition);
    }
    setNewArcticle(arcticleCurrentPosition);
  }

  function setNewArcticle(position){
    arcticleHead.innerHTML = ArrayOfArcticles[position].headline.main;
    console.log(ArrayOfArcticles[position].headline.main, arcticleHead);
    arcticleSnippet.innerHTML = ArrayOfArcticles[position].abstract;
    arcticleDate.innerHTML = ArrayOfArcticles[position].pub_date;

  }

  leftButtonClick.addEventListener('click', onLeftButtonClick);
  rightButtonClick.addEventListener('click', onRightButtonClick);
