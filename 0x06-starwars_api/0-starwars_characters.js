#!/usr/bin/node

const util = require('util');
const request = util.promisify(require('request'));

if (process.argv.length !== 3 || isNaN(parseInt(process.argv[2]))) {
  console.error('Usage: ./starWarsCharacters.js <Film_ID>');
  process.exit(1);
}

const filmID = parseInt(process.argv[2]);

async function starwarsCharacters (filmId) {
  try {
    const endpoint = `https://swapi-api.hbtn.io/api/films/${filmId}`;
    const response = await request(endpoint);
    const filmData = JSON.parse(response.body);

    if (!filmData.characters || filmData.characters.length === 0) {
      console.log('No characters found for the given film ID.');
      return;
    }

    for (const urlCharacter of filmData.characters) {
      const characterResponse = await request(urlCharacter);
      const character = JSON.parse(characterResponse.body);
      console.log(character.name);
    }
  } catch (error) {
    console.error('Error:', error.message);
    process.exit(1);
  }
}

starwarsCharacters(filmID);
