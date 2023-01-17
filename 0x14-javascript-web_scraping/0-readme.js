#!/usr/bin/node
// reads and prints the content of a file

const fs = require('fs').promises;

const filename = process.argv[2];

fs.readFile(filename, 'utf-8')
  .then((text) => {
    process.stdout.write(text);
  })
  .catch((err) => console.log(err));
