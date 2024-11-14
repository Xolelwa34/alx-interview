#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

request(`https://swapi.dev/api/films/${movieId}/`, { json: true }, (err, res, body) => {
    if (err) { return console.log(err); }
    const characters = body.characters;

    characters.forEach(characterUrl => {
        request(characterUrl, { json: true }, (err, res, body) => {
            if (err) { return console.log(err); }
            console.log(body.name);
        });
    });
});


