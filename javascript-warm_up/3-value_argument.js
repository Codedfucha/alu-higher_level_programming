#!/usr/bin/node
const { argv } = require('node:process');

const [, , arg] = argv;

if (arg === undefined) {
  console.log('No argument');
} else {
  console.log(arg);
}
