#!/usr/bin/node

// print square

if (!isNaN(parseInt(process.argv[2]))) {
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    const arr = [];
    for (let j = 0; j < parseInt(process.argv[2]); j++) {
      arr.push('X');
    }
    console.log(arr.join(''));
  }
} else {
  console.log('Missing size');
}
