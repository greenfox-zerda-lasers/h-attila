// 1.
var king = document.getElementById("b325");
console.log(king.innerHTML);

//2.
var conceited = document.getElementsByClassName("asteroid b326");
console.log((conceited[0].innerHTML));
// window.alert(conceited[0].innerHTML);

//3.
var container = document.getElementsByClassName("big");
for (var i=0; i<container.length; i++){
  console.log(container[i].innerHTML);
}

//4.
var conceitedKing = document.querySelectorAll("div.container > div");
for (var i=0; i<conceitedKing.length; i++){
  console.log(conceitedKing[i].innerHTML);
//  window.alert(conceitedKing[i].innerHTML);

}

//5.
var noBusiness = document.querySelectorAll("div.asteroid");
for (var i=0; i<noBusiness.length; i++){
  console.log(noBusiness[i].innerHTML);
}

//6.
var allBizniss = document.querySelector("p");
// window.alert(allBizniss.innerHTML);
console.log((allBizniss.innerHTML));
