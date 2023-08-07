const book  ={
    isAvailable: false,
    checkIn: function(){
        this.isAvailable=true;return this;}};
console.log( checkIn() );
function checkIn(){return this;}
console.log( checkIn() );