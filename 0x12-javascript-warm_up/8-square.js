#!/usr/bin/node

if (isNaN(process.argv[2])) {
  console.log('Missing size');
}
for (let i = 0; i < process.argv[2]; i++) {
  console.log('X'.repeat(parseInt(process.argv[2])));
}
