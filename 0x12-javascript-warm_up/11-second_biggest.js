#!/usr/bin/node

const arg = process.argv;
const len = process.argv.length;
let sBig = 0;
if (len > 3) {
  arg.sort(function (a, b) { return a - b; });
  sBig = arg[len - 2];
}
console.log(sBig);
