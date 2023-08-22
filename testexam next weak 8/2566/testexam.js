// numbersplit(4) -> [2,2]
// numbersplit(10) -> [5,5]
// numbersplit(11) -> [5,6]
// numbersplit(-9) -> [-5,-4]
//given a number,return an arry containing the two halves of the number. if the number is odd,make the rightmost number higher.

function numbersplit(num) {
    const half1 = Math.floor(num / 2);
    const half2 = Math.ceil(num / 2);return [half1, half2];}

  console.log(numbersplit(4));
  console.log(numbersplit(10));
  console.log(numbersplit(11));
  console.log(numbersplit(-9));
  