// 1.
var newHeadingAlert = document.querySelector('h1');
// window.alert(newHeadingAlert.innerHTML);
console.log((newHeadingAlert.innerHTML));

// 1b.
console.log(document.querySelector('h1').innerHTML);

// 2.
var firstParagraphToConsole = document.querySelector('p');
console.log(firstParagraphToConsole.innerHTML);

// 3.
var secondParagraphToAlert = document.getElementsByClassName("result");
console.log(secondParagraphToAlert[0].innerHTML);

// 3b.
console.log(document.querySelector(".result").innerHTML);

// 4.
var newHeadingAlert = document.querySelector('h1');
newHeadingAlert.innerHTML = "New content";

// 5.
var changeParagraphs = document.querySelectorAll('p');
changeParagraphs[changeParagraphs.length - 1].innerHTML = changeParagraphs[0].innerHTML;
