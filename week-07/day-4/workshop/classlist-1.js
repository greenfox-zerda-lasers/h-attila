// 1.
var myClassList = document.querySelectorAll('p');
if (myClassList[2].classList.contains('cat')){
  window.alert('YEAH CAT!')
}

// 2.
if (myClassList[3].classList.contains('dolphin')){
  if (myClassList[0].classList.add('pear'));
  if (myClassList[0].classList.remove('apple'));
}

// 3.
if (myClassList[0].classList.contains('apple')){
  myClassList[2].innerHTML = 'dog';
}

// 4.
myClassList[3].style.backgroundColor = 'red';

// 5.
myClassList[1].style.borderRadius = '0';
