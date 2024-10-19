const axios = require('axios');
const qs = require('qs');
const XLSX = require('xlsx');
const fs = require('fs');
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

// Function to fetch artist info
const fetchArtistInfo = async (artistName) => {
    try {
        const token = await getAccessToken();
        if (token) {
            const artists = await searchArtistByName(artistName, token);
            if (artists.length > 0) {
                const artistInfo = await getArtistById(artists[0].id, token); // Get info for the first matched artist
                return artistInfo; // Return artist info
            } else {
                console.log('No artist found with that name.');
            }
        }
    } catch (error) {
        console.error('Error fetching artist info:', error);
    }
};

// Read artists from Excel file
const readArtistsFromExcel = (filePath) => {
    const workbook = XLSX.readFile(filePath);
    const sheetName = workbook.SheetNames[0]; // Assuming data is in the first sheet
    const sheet = workbook.Sheets[sheetName];
    const data = XLSX.utils.sheet_to_json(sheet);

    return data; // Returns an array of objects
};

// Function to save artist info to CSV
const saveToCSV = (data, fileName) => {
    const csvHeader = 'Artist ID, Artist Name, Popularity, Genres, Images\n';
    const csvRows = data
        .map((artist) => {
            const genres = artist.genres ? artist.genres.join(' || ') : 'N/A';
            // const images = artist.images && artist.images.length > 0
            //     ? artist.images.map(img => img.url).join(', ')
            //     : 'No image available'; // Ensure images exist before accessing length
            return `${artist.id}, ${artist.name}, ${artist.popularity}, ${genres}, ${artist.images}`;
        })
        .join('\n');

    fs.writeFileSync(fileName, csvHeader + csvRows, 'utf8');
};

// Function to save artist info to Excel
const saveToExcel = (data, fileName) => {
    const ws = XLSX.utils.json_to_sheet(data);
    const wb = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(wb, ws, 'Artists');
    XLSX.writeFile(wb, fileName);
};

// Main function to get artist info and save to files
const getInfo = async (filePath) => {
    try {
        const artistsExcel = readArtistsFromExcel(filePath);
        const artistInfoList = [];
        const token = await getAccessToken();
        if (!token) return;

        for (const artistExcel of artistsExcel) {
            const artistName = artistExcel.Name; // Assuming the artist name is in the 'Name' column
            const artistInfo = await fetchArtistInfo(artistName);
            if (artistInfo) {
                const imgs = artistInfo.images.map((img) => `${img.url} (size: ${img.height})`).join(' || ');
                // const imgs = artistInfo.images.map((img) => img.url).join(' || ');
                console.log(artistInfo.images);
                artistInfoList.push({
                    id: artistInfo.id,
                    name: artistInfo.name,
                    popularity: artistInfo.popularity,
                    genres: artistInfo.genres,
                    images: imgs,
                });
            }
        }

        // Save to CSV and Excel
        saveToCSV(artistInfoList, 'D:/DUT/NAM4-KI1/PBL6/CRAWL/crawl-data-from-spotify/Data-Artist/inf.csv');
        saveToExcel(artistInfoList, 'D:/DUT/NAM4-KI1/PBL6/CRAWL/crawl-data-from-spotify/Data-Artist/inf.xlsx');

        console.log('Artist information saved to artist_info.csv and artist_info.xlsx');
    } catch (error) {
        console.error('Error fetching artist albums:', error);
    }
};

// Specify the path to your Excel file containing artist names
const filePath = 'D:/DUT/NAM4-KI1/PBL6/CRAWL/crawl-data-from-spotify/Data-Artist/artist.xlsx';
getInfo(filePath);
