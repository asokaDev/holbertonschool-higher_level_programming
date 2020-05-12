#!/usr/bin/node
const SquareFather = require('./5-square');

class Square extends SquareFather {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.height));
    }
  }
}

module.exports = Square;
