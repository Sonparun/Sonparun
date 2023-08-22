//Given an array of nums,create a function that returns the total volume of all those nums combined together.A box is represented by an array with three elements:lenght, width and height
//for instance,totalVolume([2,3,2].[6,6,7],[1,2,1]) should return 266
//since(2x3x2)+(6x6x7)+(1x2x1)=12+252+2=266.

//totalVolume([4,2,4],[3,3,3],[1,1,2],[2,1,1]) -> 63
//totalVolume([2,2,2],[2,1,1]) -> 10
//totalVolume([1,1,1]) -> 1


// function sum(...args) {
//     let sum = 0;
//     for (let arg of args) sum += arg;
//     return sum;
//   }
  
//   let x = sum(4, 9, 16, 25, 29, 100, 66, 77);
//   console.log(sum)

function totalVolume(nums) {
    let sum = 0;
    for (let i = 0; i < nums.length; i++) {
      const volume = nums[i][0] * nums[i][1] * nums[i][2];
      sum += volume;}return sum;}


  console.log(totalVolume([[4,2,4],[3,3,3],[1,1,2],[2,1,1]]));
  console.log(totalVolume([[2,2,2],[2,1,1]]));
  console.log(totalVolume([[1,1,1]]));