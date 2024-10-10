#!/usr/bin/node
const { argv } = require('node:process');
const argCount = argv.length - 2;

if (argCount === 0) {
  console.log('undefined is undefined');
} else if (argCount === 1) {
  console.log(`${argv[2]} is undefined`);
} else {
  console.log(`${argv[2]} is ${argv[3]}`);
}
