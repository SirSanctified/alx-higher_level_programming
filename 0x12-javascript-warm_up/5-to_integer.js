#!/usr/bin/node

// convert to integer

if (!isNaN(parseInt(process.argv[2]))) {
  console.log(`My number: ${parseInt(process.argv[2])}`);
} else {
  console.log('Not a number');
}
