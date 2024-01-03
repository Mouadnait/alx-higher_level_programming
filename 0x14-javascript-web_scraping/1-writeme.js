#!/usr/bin/node
const fs = require('fs');

// The first argument is the file path
const file = process.argv[2];
// The second argument is the string to write
const text = process.argv[3];
// The content of the file must be written in utf-8
fs.writeFile(file, text, 'utf-8',
  function (err) {
    if (err) {
      console.log(err);
    }
  });
