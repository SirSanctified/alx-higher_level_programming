#!/usr/bin/node
// Write a string to a file.

const fs = require('fs');
const file = process.argv[2];
const str = process.argv[3];

fs.writeFile(file, str, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
