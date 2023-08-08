function promiseTimeout(ms){return new Promise((resolve,reject)=>{setTimeout(resolve,ms);});}
async function run(){console.log('Start!!');const response=await longRunningOperation();console.log(response);console.log('Stop!!');}
run();