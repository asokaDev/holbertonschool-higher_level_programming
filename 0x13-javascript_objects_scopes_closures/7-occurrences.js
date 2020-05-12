#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (let i of list) {
    if (i === searchElement) {
      counter++;
    }
  }
  return counter;
};