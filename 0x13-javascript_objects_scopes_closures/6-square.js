#!/usr/bin/node

// extend the rectangle class

const Rectangle = require('./5-square.js');

class Square extends Rectangle {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        if (!c) {
          process.stdout.write('X');
        } else {
          process.stdout.write(c);
        }
      }
      console.log();
    }
  }
}

module.exports = Square;
