#!/usr/bin/node

const fs = require('fs');

const fileA = fs.readFileSync(`./${process.argv[2]}`, 'utf8');
const fileB = fs.readFileSync(`./${process.argv[3]}`, 'utf8');
const fileConcat = fileA + fileB;

fs.writeFile(`${process.argv[4]}`, fileConcat, (err) => {
  if (err) {
    console.log(err);
  }
});
