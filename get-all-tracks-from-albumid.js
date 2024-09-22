const axios = require('axios');
const qs = require('qs');
const xlsx = require('xlsx');
require('dotenv').config()

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

    // Define the filename
    const filename = `${albumName}_${albumId}`;

    // Export to Excel
    const ws = xlsx.utils.json_to_sheet(data);
    const wb = xlsx.utils.book_new();
    xlsx.utils.book_append_sheet(wb, ws, 'Tracks');
    xlsx.writeFile(wb, `./Data/tracks-from-album/${filename}.xlsx`);

    // Export to CSV (using xlsx)
    const csv = xlsx.utils.sheet_to_csv(ws);
    require('fs').writeFileSync(`./Data/tracks-from-album/${filename}.csv`, csv);
    console.log('CSV file was written successfully');
};

// Example usage with album ID input
const fetchTracksFromAlbum = async (albumId, albumName) => {
    try {
        const token = await getAccessToken();
        if (token) {
            const tracks = await getTracksByAlbumId(albumId, token);
            if (tracks) {
                exportTracks(tracks, albumName, albumId);
            }
        }
    } catch (error) {
        console.error('Error fetching tracks from album:', error);
    }
};

// Call this function with a specific album ID and name
fetchTracksFromAlbum('4faMbTZifuYsBllYHZsFKJ', 'Ai Cũng Phải Bắt Đầu Từ Đâu Đó'); // Replace 'AlbumName' with the actual album name
