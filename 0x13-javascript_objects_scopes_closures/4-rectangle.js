#!/usr/bin/node
//  a class Rectangle that defines a rectangle//
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || typeof w !== 'number' || h <= 0 || typeof h !== 'number') {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let v1 = 0; v1 < this.height; v1++) {
      let s = '';
      for (let v2 = 0; v2 < this.width; v2++) {
        s += 'X';
      }
      console.log(s);
    }
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  rotate () {
    const t = this.width;
    this.width = this.height;
    this.height = t;
  }
};
