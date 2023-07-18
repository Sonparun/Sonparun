let furniture=['Table', 'Chairs', 'Couch'];
for (let i=0; i<furniture.length; i++) {let item = furniture[i];let letters = item.split('');
  console.log(`Letters in ${item}:`);
  for (let j = 0; j < letters.length; j++) {console.log(letters[j]);}console.log('');}