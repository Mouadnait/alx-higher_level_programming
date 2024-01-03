#!/usr/bin/node
const fs = require('fs');

// Get the file path from the command line arguments
const filePath = process.argv[2];
// Read the file asynchronously with utf-8 encoding
if (filePath) {
    fs.readFile(filePath, 'utf-8', function (err, data) {
        // If an error occurred during the reading, print the error object
        err ? console.log(err) : console.log(data);
    });
}
