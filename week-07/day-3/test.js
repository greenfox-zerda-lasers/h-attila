var converter = {}

converter.int2roman = function (number) {
  if (number < 5000) {
    var arr = String(number).split("");
    var last = arr.length-1;
    var string = "";
    var i, k, num;
    var roman = [{1: "I", 4: "IV", 5: "V", 9: "IX"},
                {1: "X", 4: "XL", 5: "L", 9: "XC"},
                {1: "C", 4: "CD", 5: "D", 9: "CM"},
                {1: "M", 4: "MMMM"}];

    for (i = last, r = 0; i >= 0; i--, r++) {
      num = parseInt(arr[i]);
      if (num >=1 && num < 4) {
        string = roman[r][1].repeat(num) + string;
      } else if (num == 4) {
        string = roman[r][4] + string;
      } else if (num > 4 && num < 9) {
        string = roman[r][5] + roman[r][1].repeat(num-5) + string;
      } else if (num == 9) {
        string = roman[r][9] + string;
      }
    }
    return string;
  } else {
    return "Your number must be under 5000!";
  }
};

console.log(converter.int2roman(4999));
