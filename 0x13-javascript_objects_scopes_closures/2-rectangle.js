#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (parseInt(w) > 0 && parseInt(h) > 0) {
      this.height = h;
      this.width = w;
    }
  }
}

module.exports = Rectangle;
