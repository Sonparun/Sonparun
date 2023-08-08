const promise=new Promise((resovle,reject)=>{const res=true;
if(res){resovle('Resolved!');}else{reject(Errpr('Fatal Error'));}});
promise.then((res)=>console.log(res),(err)=>console.log(err));