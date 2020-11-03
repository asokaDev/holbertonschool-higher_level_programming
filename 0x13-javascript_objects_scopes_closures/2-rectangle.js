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
}

module.exports = Rectangle;
