#!/usr/bin/node
const fs = require('fs');

// Get the file path from the command line arguments
const filePath = process.argv[2];
// Read the file asynchronously with utf-8 encoding
if (filePath) {
    fs.readFile(filePath, 'utf-8', (err, data) => {
        err ? console.log(err) : console.log(file);
    });
}
