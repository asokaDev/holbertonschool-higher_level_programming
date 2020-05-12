#!/usr/bin/node

exports.converter = (base) => {
  return (n) => n.toString(base);
};
