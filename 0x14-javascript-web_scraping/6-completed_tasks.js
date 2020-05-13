#!/usr/bin/node

const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const arr = JSON.parse(body);
    console.log(arr.reduce((obj, el) => {
      if (el.completed) {
        obj[el.userId] ? obj[el.userId]++ : obj[el.userId] = 1;
      }
      return obj;
    }, {}));
  }
});
