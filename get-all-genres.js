const axios = require('axios');
const qs = require('qs');
require('dotenv').config();

// Spotify API credentials
const clientId = process.env.CLIENT_ID;
const clientSecret = process.env.CLIENT_SECRET;

// Function to get access token from Spotify API
const getAccessToken = async () => {
    const tokenUrl = 'https://accounts.spotify.com/api/token';
    const headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        Authorization: 'Basic ' + Buffer.from(clientId + ':' + clientSecret).toString('base64'),
    };

    const data = qs.stringify({
        grant_type: 'client_credentials',
    });

    try {
        const response = await axios.post(tokenUrl, data, { headers });
        return response.data.access_token;
    } catch (error) {
        console.error('Error getting access token:', error);
    }
};

// Function to search for an artist by name
const searchArtistByName = async (artistName, token) => {
    const searchUrl = `https://api.spotify.com/v1/search?q=${encodeURIComponent(artistName)}&type=artist`;

    const headers = {
        Authorization: `Bearer ${token}`,
    };

    try {
        const response = await axios.get(searchUrl, { headers });
        return response.data.artists.items; // Return list of artists found
    } catch (error) {
        console.error('Error searching for artist:', error);
    }
};

// Function to fetch artist information by artist ID
const getArtistById = async (artistId, token) => {
    const artistUrl = `https://api.spotify.com/v1/artists/${artistId}`;

    const headers = {
        Authorization: `Bearer ${token}`,
    };

    try {
        const response = await axios.get(artistUrl, { headers });
        return response.data; // Return artist information
    } catch (error) {
        console.error('Error fetching artist:', error);
    }
};

// Function to fetch genres of an artist
const fetchGenres = async (artistName) => {
    try {
        const token = await getAccessToken();
        if (token) {
            const artists = await searchArtistByName(artistName, token);
            if (artists.length > 0) {
                const artistInfo = await getArtistById(artists[0].id, token);
                if (artistInfo) {
                    console.log(`Genres for artist ${artistInfo.name}: ${artistInfo.genres.join(', ')}`);
                }
            } else {
                console.log('No artist found with that name.');
            }
        }
    } catch (error) {
        console.error('Error fetching genres:', error);
    }
};

// Example usage: fetch genres for a specific artist
fetchGenres('hieu thu hai'); // Replace 'Adele' with the actual artist name you want to search for

// Get all genres from spotify
// https://api.spotify.com/v1/recommendations/available-genre-seeds
