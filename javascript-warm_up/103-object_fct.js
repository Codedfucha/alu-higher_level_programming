#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12,
  // Add a method incr that increments the value property
  incr: function () {
    this.value++;
  }
};

console.log(myObject);

// Calling the incr function to increment the value property
myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);
