class Dog{constructor(name){this._name=name;}intrudce(){console.log('This is'+ this._name+' !');}static bark(){console.log('Woof!');}}
const myDog=new Dog('Buster');
myDog.intrudce();
Dog.bark();