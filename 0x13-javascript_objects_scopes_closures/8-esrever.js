#!/usr/bin/node

exports.esrever = function (list) {
  return list.reduce((accumulator, currentValue) => {
    accumulator.unshift(currentValue);
    return accumulator;
  }, []);
};
