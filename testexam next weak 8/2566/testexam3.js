//create a function that moves all capital letters to the front of a word.

//capToFront("hApPy") -> "APhpy"
//capToFront("moveMENT") -> "MENTmove"
//capToFront("shOrtCAKE") -> "OCAKEshrt"


function capToFront(str){
    let Bigletter = '';
    let Smallletter = '';
    for (let i = 0; i < str.length; i++){
      if (str[i] >='A'&& str[i]<='Z'){
        Bigletter += str[i];
      }else{Smallletter += str[i];}}return Bigletter+Smallletter;}

  console.log(capToFront("hApPy"));
  console.log(capToFront("moveMENT"));
  console.log(capToFront("shOrtCAKE"));