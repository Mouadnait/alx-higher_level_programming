#!/usr/bin/node
const fs = require('fs');

// The first argument is the file path
const filePath = process.argv[2];
// The second argument is the string to write
const contentToWrite = process.argv[3];
// Write to the file asynchronously with utf-8 encoding
fs.writeFile(filePath, contentToWrite, 'utf-8', (err) => err ? console.log(err) : '');
