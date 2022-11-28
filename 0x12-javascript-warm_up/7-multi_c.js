#!/usr/bin/node

// dynamic print

if (!isNaN(parseInt(process.argv[2]))) {
  let i = 0;
  while (i < parseInt(process.argv[2])) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
