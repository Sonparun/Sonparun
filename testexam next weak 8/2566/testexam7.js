//Create a function that takes an array of numbers and returns the sum of the two lowest positive numbers.

//sumTwoSmallestNums([19,5,42,2,77]) -> 7
//sumTwoSmallestNums([10,343445353,3453445,3453545353453]) -> 3453455
//sumTwoSmallestNums([2,9,6,-1]) -> 8
//sumTwoSmallestNums([879,953,694,-847,342,221,-91,-723,791,-587]) -> 
//sumTwoSmallestNums([3683,2902,3951,-475,1617,-2385]) -> 4519

function sumTwoSmallestNums(arr) {
    const positiveNumbers = arr.filter(num => num > 0).sort((a, b) => a - b);return positiveNumbers[0] + positiveNumbers[1];}
  
  console.log(sumTwoSmallestNums([19, 5, 42, 2, 77]));
  console.log(sumTwoSmallestNums([10, 343445353, 3453445, 3453545353453]));
  console.log(sumTwoSmallestNums([2, 9, 6, -1]));
  console.log(sumTwoSmallestNums([879, 953, 694, -847, 342, 221, -91, -723, 791, -587]));
  console.log(sumTwoSmallestNums([3683, 2902, 3951, -475, 1617, -2385]));
  