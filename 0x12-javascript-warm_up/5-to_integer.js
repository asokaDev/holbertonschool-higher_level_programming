#!/usr/bin/node

if (isNaN(parseInt(process.argv[2]))) {
  console.log('Not a number');
} else {
  const num = Math.floor(process.argv[2]);
  console.log(`My number: ${num}`);
}
