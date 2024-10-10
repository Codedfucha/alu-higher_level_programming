#!/usr/bin/node

const { argv } = require('node:process');
const argCount = argv[2];

if (argCount === undefined || (isNaN(argCount))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < argCount; i++) {
    console.log('C is fun');
  }
}
