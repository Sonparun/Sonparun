function criticalCode(){throw'throwing an exception';}
function logError(theException){console.log(theException);}
console.log('\n***Try..Catch***\n')
try{criticalCode();}catch(ex){console.log('Got an error');logError.apply(ex);}
console.log('\n***Throwing in Try..Catch***\n')
try{throw'An exveption that is thrown every time';}catch(ex){console.log('Got an error');logError(ex);}
console.log('\n***Try..Catch..Finally***\n')
try{criticalCode();}catch(ex){console.log('Got an Error');logError(ex);}finally{console.log('Code that alaways will run');}
function hello(){console.log('\n***Throwing Exceptions***\n')}

