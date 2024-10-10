#!/usr/bin/node
// Define the function that increments and calls the given function
exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
