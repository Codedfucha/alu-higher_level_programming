#!/usr/bin/node
const fs = require('fs');

// Get the file paths from command line arguments
const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

// Read the first source file
fs.readFile(sourceFile1, 'utf8', (err, data1) => {
    if (err) {
        console.error(`Error reading ${sourceFile1}:`, err);
        return;
    }

    // Read the second source file
    fs.readFile(sourceFile2, 'utf8', (err, data2) => {
        if (err) {
            console.error(`Error reading ${sourceFile2}:`, err);
            return;
        }

        // Concatenate the contents and write to the destination file
        const concatenatedData = data1 + '\n' + data2;
        fs.writeFile(destinationFile, concatenatedData, (err) => {
            if (err) {
                console.error(`Error writing to ${destinationFile}:`, err);
                return;
            }
            console.log(`Successfully concatenated ${sourceFile1} and ${sourceFile2} into ${destinationFile}`);
        });
    });
});

