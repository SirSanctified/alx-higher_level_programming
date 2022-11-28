#!/usr/bin/node

// compute factorial

const num = process.argv[2];

function factorial (number) {
  if (isNaN(number) || number === 0 || number === 1) {
    return 1;
  }
  return number * factorial(number - 1);
}

console.log(factorial(num));
