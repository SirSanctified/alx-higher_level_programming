#!/usr/bin/node

// command-line arguments

const args = process.argv;

if (args.length - 2 === 0) {
  console.log('No arguments');
} else if (args.length - 2 === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
