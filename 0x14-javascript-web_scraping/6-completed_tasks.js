#!/usr/bin/node

const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const arr = JSON.parse(body);
    console.log(arr.reduce((obj, elem) => {
      if (elem.completed) {
        ret[elem.userId] ? ret[elem.userId]++ : ret[elem.userId] = 1;
      }
      return ret;
    }, {}));
  }
});
