#!/usr/bin/node

const request = require('request');
const episodeId = String(process.argv[2]);
const requestURL = 'https://swapi-api.hbtn.io/api/films/';
const filmURL = 'https://swapi-api.hbtn.io/api/films/' + episodeId + '/';

request(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jsonBodyFilms = JSON.parse(body).results;
    const numberFilms = jsonBodyFilms.length;
    for (let filmIdx = 0; filmIdx < numberFilms; filmIdx++) {
      if (String(jsonBodyFilms[filmIdx].url) === filmURL) {
        const lsCharacters = jsonBodyFilms[filmIdx].characters;
        const numCharacters = lsCharacters.length;
        for (let index = 0; index < numCharacters; index++) {
          request(lsCharacters[index], function (error, response, body) {
            if (error) {
              console.log(error);
            } else {
              console.log(JSON.parse(body).name);
            }
          });
        }
        break;
      }
    }
  }
});
