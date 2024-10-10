#!/usr/bin/node
// Define the function that executes the given function x times
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};

