//Create the function that takes an array with objects and returns the sum of people's budgets.


//getBudgets([
//     {name:"John",age:21,budget:23000},
//     {name:"Steve",age:32,budget:40000},
//     {name:"Martin",age:16,budget:2700}
// ]) -> 65700


//getBudgets([
//     {name:"John",age:21,budget:29000},
//     {name:"Steve",age:32,budget:32000},
//     {name:"Martin",age:16,budget:1600}
// ]) -> 65700


function getBudgets(people) {
    let totalBudget = 0;
    for (let i = 0; i < people.length; i++) {
      totalBudget += people[i].budget;
    }
    return totalBudget;
  }
  
  const people1 = [
    { name: "John", age: 21, budget: 23000 },
    { name: "Steve", age: 32, budget: 40000 },
    { name: "Martin", age: 16, budget: 2700 }
  ];
  console.log(getBudgets(people1));
  
  const people2 = [
    { name: "John", age: 21, budget: 29000 },
    { name: "Steve", age: 32, budget: 32000 },
    { name: "Martin", age: 16, budget: 1600 }
  ];
  console.log(getBudgets(people2));