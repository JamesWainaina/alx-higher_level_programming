#!/usr/bin/node

class Square extends require('./5-square') {
  charPrint (c) {
    let cprint = c;
    if (cprint === undefined) {
      cprint = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(cprint.repeat(this.width));
    }
  }
}
module.exports = Square;
