#!/usr/bin/node

const fetch = require('node-fetch');

// Check if a movie ID is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./100-starwars_characters.js <Movie ID>');
  process.exit(1);
}

// Get the movie ID from command-line arguments
const movieID = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieID}/`;

// Fetch movie details from Star Wars API
fetch(apiUrl)
  .then(response => {
    if (!response.ok) {
      throw new Error('Failed to fetch data');
    }
    return response.json();
  })
  .then(data => {
    const characters = data.characters;
    // Fetch each character's name
    characters.forEach(characterUrl => {
      fetch(characterUrl)
        .then(response => response.json())
        .then(characterData => {
          console.log(characterData.name);
        })
        .catch(err => {
          console.error('Error fetching character data:', err);
        });
    });
  })
  .catch(err => {
    console.error('Error fetching movie data:', err);
  });

