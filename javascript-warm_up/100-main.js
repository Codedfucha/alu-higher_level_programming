#!/usr/bin/node
myVar = 89;
require('./100-let_me_const');  // This will load the file that modifies myVar
console.log(myVar);  // This will print the modified value of myVar

