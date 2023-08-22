//Create a function that takes a string (IPv4 address in standard dot-decimal format) and returns true if the IP is valid or flase if it's not.For informaton on IPv4 formatting please refer to the resources in the Resources tab.

//isValidIP("1.2.3.4") -> true
//isValidIP("1.2.3") -> false
//isValidIP("1.2.3.4.5") -> false
//isValidIP("123.45.67.89") -> true
//isValidIP("123.456.78.90") -> false
//isValidIP("123.045.067.089") -> false

function isValidIP(ip) {
    const parts = ip.split('.');
    
    if (parts.length !== 4) {
      return false;
    }
    
    for (const part of parts) {
      if (!/^\d{1,3}$/.test(part)) {
        return false;
      }
      
      const num = parseInt(part, 10);
      if (num < 0 || num > 255 || (part.length > 1 && part[0] === '0')) {
        return false;
      }
    }
    
    return true;
  }
  console.log(isValidIP("125.222.3.4"));
  
  console.log(isValidIP("1.2.3.4"));
  console.log(isValidIP("1.2.3"));
  console.log(isValidIP("1.2.3.4.5"));
  console.log(isValidIP("123.45.67.89"));
  console.log(isValidIP("123.456.78.90"));
  console.log(isValidIP("123.045.067.089"));
  


  