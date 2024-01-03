#!/usr/bin/node
const process = require('process');
const request = require('request');

// The first argument is the URL to request (GET)
const url = process.argv[2];
// Make a GET request and display the status code
request.get(url, (error, response) => {
  error ? console.log(error) : console.log(`code: ${response.statusCode}`);
});
