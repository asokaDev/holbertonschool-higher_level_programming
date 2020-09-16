#!/usr/bin/node

const num = parseInt(process.argv[2]);
isNaN(num) ? console.log('Not a number') : console.log(`My number: ${num}`);
