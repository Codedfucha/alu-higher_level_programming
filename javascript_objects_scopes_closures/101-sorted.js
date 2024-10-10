#!/usr/bin/node
const { dict } = require('./101-data');

// Create a new dictionary to hold occurrences
const occurrences = {};

// Iterate through the original dictionary
for (const userId in dict) {
    const count = dict[userId]; // Get the occurrence count

    // If the count does not exist in occurrences, initialize it
    if (!occurrences[count]) {
        occurrences[count] = [];
    }

    // Add the user ID to the corresponding count array
    occurrences[count].push(userId);
}

// Print the new dictionary
console.log(occurrences);
