#!/usr/bin/node

// print values of command line arguments

if (process.argv.slice(2)[0] !== undefined) {
  process.argv.slice(2).forEach(i => {
    console.log(i);
  });
} else {
  console.log('No argument');
}
