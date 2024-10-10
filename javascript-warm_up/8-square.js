#!/usr/bin/node

const { argv } = require('node:process');
const argCount = parseInt(argv[2]);

if (isNaN(argCount)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < argCount; i++) {
    let row = '';
    for (let j = 0; j < argCount; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
