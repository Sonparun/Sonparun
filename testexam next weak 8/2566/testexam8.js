//Given an array of integers arr and an integer n,find out a pair of numbers [x,y]from a given array such that x*y=n.
//if the pair is not found, return null

//simplePair([1,2,3],3) ->[1,3]
//simplePair([1,2,3],6) ->[2,3]
//simplePair([1,2,3],9) -> null

function simplePair(arr, n) {
    for (let i = 0; i < arr.length; i++) {
      for (let j = i + 1; j < arr.length; j++) {
        if (arr[i] * arr[j] === n) {
          return [arr[i], arr[j]];}}}return null; }
  
  console.log(simplePair([1, 2, 3], 3));
  console.log(simplePair([1, 2, 3], 6));
  console.log(simplePair([1, 2, 3], 9));
  console.log(simplePair([1, 2, 3, 4, 5, 6], 30));