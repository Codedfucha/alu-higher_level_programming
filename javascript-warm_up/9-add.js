#!/usr/bin/node
const { argv } = require('node:process');

function add (a, b) {
  return a + b;
}
const argCount = argv.length - 2;

if (argCount <= 1) {
  console.log('NaN');
} else {
  const num1 = Number(argv[2]);
  const num2 = Number(argv[3]);
  const answer = add(num1, num2);
  console.log(answer);
}
