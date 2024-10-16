#!/usr/bin/node

const request = require('request');  // Import the request module
const movieId = process.argv[2];     // Get the movie ID from the command-line argument

// Check if the movie ID is provided
if (!movieId) {
  console.error('Usage: ./101-starwars_characters.js <movie_id>');
  process.exit(1);
}

// Star Wars API URL to fetch movie details
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make the request to the movie endpoint
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the body of the response to JSON
  const film = JSON.parse(body);
  const characters = film.characters;

  // For each character, fetch and print the name
  characters.forEach((characterUrl) => {
    request(characterUrl, function (err, res, characterBody) {
      if (err) {
        console.error(err);
        return;
      }

      const character = JSON.parse(characterBody);
      console.log(character.name);  // Print the character name
    });
  });
});

