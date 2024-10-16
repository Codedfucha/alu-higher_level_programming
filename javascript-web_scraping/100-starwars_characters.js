#!/usr/bin/node
const request = require('request');

// Movie ID from command-line arguments
const movieId = process.argv[2];

// URL for fetching data
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Make the request to the Star Wars API to get movie data
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Parse the body as JSON to work with the data
  const movieData = JSON.parse(body);

  // Loop through each character URL in the film data
  const characters = movieData.characters;
  characters.forEach((characterUrl) => {
    // For each character URL, make a request to get the character name
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error:', charError);
        return;
      }

      // Parse and print each character's name
      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
    });
  });
});

