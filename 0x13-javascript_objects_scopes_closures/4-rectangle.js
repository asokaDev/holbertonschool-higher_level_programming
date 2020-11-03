#!/usr/bin/node

class Rectangle {
  constructor (_width, _heigh) {
    if (isNaN(_width) || isNaN(_heigh) ||
        _width <= 0 || _heigh <= 0) {
      return;
    }
    this.width = _width;
    this.height = _heigh;
  }

  print () {
    let i = 0;
    while (i < this.height) {
      console.log('X'.repeat(this.width));
      i++;
    }
  }

  rotate () {
    const __width = this.width;
    this.width = this.height;
    this.height = __width;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
