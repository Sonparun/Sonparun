//The function is given a string.Sort the characters and return a new string.Sorting conditions:
//Most frequent(case-specific) move in front.
//For the same frequency upper case characters move in front.
//For the same frequency andcase sort them alphabetically.

//frequencySort("tree") -> "eert"
//frequencySort("cccaaa") -> "aaaccc"
//frequencySort("Aabb") -> "bbAa"

function frequencySort(string) {
    const charCount = {};
    string.split('').forEach(char => charCount[char] = (charCount[char] || 0) + 1);
    return string.split('').sort((a, b) =>charCount[b] - charCount[a] || a.localeCompare(b, 'en', { sensitivity: 'case', usage: 'sort' })).join('');}
  
  console.log(frequencySort("tree"));
  console.log(frequencySort("cccaaa"));
  console.log(frequencySort("Aabb"));
  console.log(frequencySort("abcABC"));
  console.log(frequencySort("ZzhHYyLl")); 
  console.log(frequencySort("IWANTtofuckYOURASS")); 