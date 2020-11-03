#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.reduce((accumulator, currentValue) => {
    if (currentValue === searchElement) {
      accumulator++;
    }
    return accumulator;
  }, 0);
};
