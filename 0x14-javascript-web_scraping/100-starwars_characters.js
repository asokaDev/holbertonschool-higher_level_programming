#!/usr/bin/node

const request = require('request');
request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, (error, res, body) => {
  if (error) {
    console.log(error);
  } else {
    const characters  = JSON.parse(body).characters;
    characters .forEach(char => {
      request(char, (error, res, body) => {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
