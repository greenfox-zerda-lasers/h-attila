function getArcticlesFromNYT(){
  var httpRequest = new XMLHttpRequest();
  httpRequest.open('GET', 'https://api.nytimes.com/svc/search/v2/articlesearch.json?api-key=ecf5a7de7cc04cb2b96621ac0933ae26&q=apollo+11+moon', true);
  httpRequest.send();
  httpRequest.onreadystatechange = function(){
    if (httpRequest.readyState === XMLHttpRequest.DONE){
      var dataFromNYT = JSON.parse(httpRequest.response).response.docs;
      showInfoOnScreen(dataFromNYT);
    }
  };
}

function showInfoOnScreen(dataFromNYT){
  dataFromNYT.forEach(function(article){
    var arcicleContent = document.querySelector('.articles');
    var newArticleItem = document.createElement('article');
    var newArticleHeadline = document.createElement('a');
    var newArticleSnippet = document.createElement('p');
    var newArticleDate = document.createElement('p');

    newArticleHeadline.innerHTML = article.headline.main;
    newArticleHeadline.href = article.web_url;
    newArticleSnippet.innerHTML = article.snippet;
    newArticleDate.innerHTML = article.pub_date;

    newArticleItem.appendChild(newArticleHeadline);
    newArticleItem.appendChild(newArticleSnippet);
    newArticleItem.appendChild(newArticleDate);

    arcicleContent.appendChild(newArticleItem);
  });
}

getArcticlesFromNYT();
