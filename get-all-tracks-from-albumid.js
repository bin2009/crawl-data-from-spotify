const axios = require('axios');
const qs = require('qs');
const xlsx = require('xlsx');
const fs = require('fs');
require('dotenv').config();

// Spotify API credentials
const clientId = process.env.CLIENT_ID;
const clientSecret = process.env.CLIENT_SECRET;

// replace
let nameFolder = 'Phương Ly';

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

// Function to fetch all tracks from a given album ID
const getTracksByAlbumId = async (albumId, token) => {
    const tracksUrl = `https://api.spotify.com/v1/albums/${albumId}/tracks`;

    const headers = {
        Authorization: `Bearer ${token}`,
    };

    try {
        const response = await axios.get(tracksUrl, { headers });
        return response.data.items; // Return tracks directly
    } catch (error) {
        console.error('Error fetching tracks:', error);
    }
};

// Function to export tracks to Excel and CSV
const exportTracks = (tracks, albumName, albumId) => {
    const data = tracks.map((track) => {
        const artists = track.artists.map((artist) => `${artist.name} (ID: ${artist.id})`).join(' || ');

        return {
            ID: track.id,
            Track: track.name,
            Artists: artists,
            DiscNumber: track.disc_number,
            TrackNumber: track.track_number,
            Duration: track.duration_ms,
            PreviewUrl: track.preview_url,
        };
    });

    // Create directory if not exists
    const folderPath = `./Data/${nameFolder}/ablum-from-artist`;
    if (!fs.existsSync(folderPath)) {
        fs.mkdirSync(folderPath, { recursive: true });
    }

    // Define the filename
    const filename = `${albumName}_${albumId}`;

    // Export to Excel
    const ws = xlsx.utils.json_to_sheet(data);
    const wb = xlsx.utils.book_new();
    xlsx.utils.book_append_sheet(wb, ws, 'Tracks');
    xlsx.writeFile(wb, `${folderPath}/${filename}.xlsx`);

    // Export to CSV (using xlsx)
    const csv = xlsx.utils.sheet_to_csv(ws);
    fs.writeFileSync(`${folderPath}/${filename}.csv`, csv);
    console.log('CSV file was written successfully');
};

// Function to read album IDs and names from an Excel file
const readAlbumsFromExcel = (filePath) => {
    const workbook = xlsx.readFile(filePath);
    const sheetName = workbook.SheetNames[0]; // Assuming data is in the first sheet
    const sheet = workbook.Sheets[sheetName];
    const data = xlsx.utils.sheet_to_json(sheet);

    return data; // Returns an array of objects
};

// Example function to fetch tracks for albums from the Excel file
const fetchTracksFromAlbumsInExcel = async (filePath) => {
    const albums = readAlbumsFromExcel(filePath);

    const token = await getAccessToken();
    if (!token) return;

    for (const album of albums) {
        const albumId = album.ID; // Assuming your Excel has an 'id' column
        const albumName = album.Album; // Assuming your Excel has a 'name' column

        if (albumId && albumName) {
            const tracks = await getTracksByAlbumId(albumId, token);
            if (tracks) {
                exportTracks(tracks, albumName, albumId);
            }
        } else {
            console.log('Missing album ID or name.');
        }
    }
};

// Call this function with the path to your Excel file
fetchTracksFromAlbumsInExcel(`./Data/${nameFolder}/${nameFolder}_albums.xlsx`);
