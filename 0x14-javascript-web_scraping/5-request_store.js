#!/usr/bin/node
// gets the contents of a webpage and stores it in a file
// usage: ./5-request_store.js <URL> <file>
// example: ./5-request_store.js http://www.google.com google.html

const request = require('request');
const fs = require('fs');

request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(process.argv[3], body, 'utf8', function (error) {
      if (error) {
        console.error(error);
      }
    });
  }
});
