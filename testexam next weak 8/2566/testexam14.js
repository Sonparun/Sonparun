//This string,"sadbpstcrdavefikkgoenqrt" has a five letter word embedded within it.
//HEre's a clue on how to find it:
//1.The str can be broken up from left to right into a series of overlapping letter triplets.
//3.The values of the triplets that contain the letters of the secret word as the middle member form an increasing arithmetic series.
//Given the str and len of the sevret word,improvise a function that finds the secret word.

//Examples
//secretWord("sadbpstcrdavefikkgoenqrt",5) -> "brake"
//sa(dbp)st(crd)(vae)f(ikk)g(oen)qrt
//The values of the triplets in parentheses are 22,25,28,31,34.
//An arithmetic series with difference of 3.

//secretWord("aheiayd",3) -> "hey"
//(a(he)i(ayd))
//The triplets with the secret letter can overlap.
//ahe=14,hei=22,ayd=30:a series with a difference of 8.

function secretWord(str, len) {
    let result = '';
    
    for (let i = 0; i <= str.length - 3 * len; i++) {
      const triplet1 = str.charCodeAt(i + len - 1) - str.charCodeAt(i + len - 2);
      const triplet2 = str.charCodeAt(i + 2 * len - 1) - str.charCodeAt(i + 2 * len - 2);
      
      if (triplet2 - triplet1 === triplet1) {
        for (let j = i + len - 1; j < str.length; j += len) {
          result += str[j];
        }
        break;
      }
    }
    
    return result;
  }
  
  console.log(secretWord("sadbpstcrdavefikkgoenqrt", 5)); // Output: "brake"
  console.log(secretWord("aheiayd", 3)); // Output: "hey"
  
  