#!/usr/bin/node
// reads and prints the content of a file

const fs = require('fs');

const filename = process.argv[2];

fs.readFile(filename, 'utf-8', (err, text) => {
  if (err) {
    console.log(err);
  } else {
    process.stdout.write(text);
  }
});
