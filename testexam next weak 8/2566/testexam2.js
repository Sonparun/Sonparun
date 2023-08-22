//crate a function that takes a number as an argument and returns the highest digit in that number.

// highestDigit(379) -> 9
// highestDigit(2) -> 2
// highestDigit(377401) -> 7


function highestDigit(num) {
    let highest = 0;
    
    while (num > 0) {
      const digit = num % 10;
      if (digit > highest) {
        highest = digit;
      }num = Math.floor(num / 10);}return highest;}

  console.log(highestDigit(379));
  console.log(highestDigit(2));
  console.log(highestDigit(377401));