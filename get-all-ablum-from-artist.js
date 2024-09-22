const axios = require('axios');
const qs = require('qs');
const XLSX = require('xlsx');
const fs = require('fs');
require('dotenv').config();

const clientId = process.env.CLIENT_ID;
const clientSecret = process.env.CLIENT_SECRET;

let nameFolder = '';

// Get access token from Spotify
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

// Search for an artist by name
const searchArtist = async (artistName, token) => {
    const searchUrl = `https://api.spotify.com/v1/search?q=${encodeURIComponent(artistName)}&type=artist`;

    const headers = {
        Authorization: `Bearer ${token}`,
    };

    try {
        const response = await axios.get(searchUrl, { headers });
        const artists = response.data.artists.items;

        if (artists.length > 0) {
            const artist = artists[0];
            console.log(`Artist Name: ${artist.name}, Artist ID: ${artist.id}`);
            return artist;
        } else {
            console.log('Artist not found');
            return {};
        }
    } catch (error) {
        console.error('Error searching for artist:', error);
    }
};

// Export data to Excel and CSV
const exportToExcelAndCsv = (albumData, artistName) => {
    if (albumData.length === 0) {
        console.log('No album data to export.');
        return;
    }

    // Convert the album data to a worksheet and create a workbook
    const ws = XLSX.utils.json_to_sheet(albumData);
    const wb = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(wb, ws, 'Albums');

    // Create directory if not exists
    const folderPath = `./Data/${nameFolder}/`;
    if (!fs.existsSync(folderPath)) {
        fs.mkdirSync(folderPath, { recursive: true });
    }

    // Save Excel file
    const excelFileName = `${folderPath}/${artistName}_albums.xlsx`;
    XLSX.writeFile(wb, excelFileName);
    console.log(`Excel file saved as: ${excelFileName}`);

    // Save CSV file
    const csvFileName = `${folderPath}/${artistName}_albums.csv`;
    // const csvFileName = `./Data/${nameFolder}/ablum-from-artist/${artistName}_albums.csv`;
    const csvData = XLSX.utils.sheet_to_csv(ws);
    fs.writeFileSync(csvFileName, csvData);
    console.log(`CSV file saved as: ${csvFileName}`);
};

// Fetch albums by artist ID
const getAlbumsByArtistId = async (artistId, token, artistName) => {
    const albumsUrl = `https://api.spotify.com/v1/artists/${artistId}/albums`;

    const headers = {
        Authorization: `Bearer ${token}`,
    };

    const params = {
        include_groups: 'album,single', // Filter albums, singles, or compilations
        limit: 50, // Max limit per request
    };

    try {
        const response = await axios.get(albumsUrl, { headers, params });
        const albums = response.data.items;

        // Collect album data
        const albumData = albums.map((album) => {
            const albumImageUrl = album.images.length > 0 ? album.images[0].url : 'No image available';
            const artists = album.artists.map((artist) => `${artist.name} (ID: ${artist.id})`).join(' || ');

            return {
                ID: album.id,
                Album: album.name,
                ReleaseDate: album.release_date,
                Artists: artists,
                AlbumType: album.album_type,
                TotalTracks: album.total_tracks,
                AlbumImage: albumImageUrl,
                Type: album.type,
            };
        });

        // Export the data to Excel and CSV files
        exportToExcelAndCsv(albumData, artistName);

        // Handle pagination for additional albums
        if (response.data.next) {
            console.log('Fetching more albums...');
            await fetchMoreAlbums(response.data.next, token, albumData, artistName);
        }
    } catch (error) {
        console.error('Error fetching albums:', error);
    }
};

// Fetch more albums for pagination
const fetchMoreAlbums = async (url, token, albumData, artistName) => {
    const headers = {
        Authorization: `Bearer ${token}`,
    };

    try {
        const response = await axios.get(url, { headers });
        const albums = response.data.items;

        // Append more albums
        const moreAlbumData = albums.map((album) => {
            const albumImageUrl = album.images.map((image) => `${image.url}`).join(' || ');
            // const albumImageUrl = album.images.length > 0 ? album.images[0].url : 'No image available';
            const artists = album.artists.map((artist) => `${artist.name} (ID: ${artist.id})`).join(' || ');

            return {
                ID: album.id,
                Album: album.name,
                ReleaseDate: album.release_date,
                Artists: artists,
                AlbumType: album.album_type,
                TotalTracks: album.total_tracks,
                AlbumImage: albumImageUrl,
                Type: album.type,
            };
        });

        albumData = albumData.concat(moreAlbumData);

        // Recursively fetch more albums if there are more pages
        if (response.data.next) {
            await fetchMoreAlbums(response.data.next, token, albumData, artistName);
        } else {
            // Once all data is fetched, export it
            exportToExcelAndCsv(albumData, artistName);
        }
    } catch (error) {
        console.error('Error fetching more albums:', error);
    }
};

// Example usage with async/await
const fetchArtistAlbums = async (artistName) => {
    try {
        const token = await getAccessToken();
        const artist = await searchArtist(artistName, token);
        nameFolder = artist.name;

        if (artist && artist.id) {
            await getAlbumsByArtistId(artist.id, token, artist.name);
        } else {
            console.log('Artist not found or no ID available.');
        }
    } catch (error) {
        console.error('Error fetching artist albums:', error);
    }
};

// Example usage
fetchArtistAlbums('phương ly'); // Replace with any artist name
