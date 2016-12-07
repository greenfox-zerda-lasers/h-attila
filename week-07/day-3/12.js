// float2string(num)

function float2string(num) {
  newString = String(num).split('.');
  return newString[0] + '.' + newString[1];
}

function string2float(str) {
  newString = str.split('.');
  return parseInt(newString[0],10) + parseInt(newString[1],10)/100;
}

console.log(float2string(11.22));
console.log(string2float('11.22'));
