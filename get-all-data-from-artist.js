const axios = require('axios');
const qs = require('qs');
const XLSX = require('xlsx');
const fs = require('fs');
require('dotenv').config();
const unidecode = require('unidecode');

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

// Hàm để thêm thời gian chờ
const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

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

    // Thêm thời gian chờ sau mỗi request
    await delay(1000);
};

const convertToNonAccented = (text) => {
    text = unidecode(text);
    text = text.replaceAll(' ', '');
    console.log(text);
    return text;
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
    XLSX.utils.book_append_sheet(wb, ws, 'Albums and Tracks');

    const nameFolderNew = convertToNonAccented(nameFolder);

    // Create directory if not exists
    const folderPath = `./Data/${nameFolderNew}`;
    if (!fs.existsSync(folderPath)) {
        fs.mkdirSync(folderPath, { recursive: true });
    }

    const artistNameSave = convertToNonAccented(artistName);

    // Save Excel file
    const excelFileName = `${folderPath}/${artistNameSave}_albums_tracks.xlsx`;
    XLSX.writeFile(wb, excelFileName);
    console.log(`Excel file saved as: ${excelFileName}`);

    // Save CSV file
    const csvFileName = `${folderPath}/${artistNameSave}_albums_tracks.csv`;
    const csvData = XLSX.utils.sheet_to_csv(ws);
    fs.writeFileSync(csvFileName, csvData);
    console.log(`CSV file saved as: ${csvFileName}`);
};

// Fetch tracks for a given album ID
const getTracksByAlbumId = async (albumId, token) => {
    const tracksUrl = `https://api.spotify.com/v1/albums/${albumId}/tracks`;
    const headers = {
        Authorization: `Bearer ${token}`,
    };

    try {
        const response = await axios.get(tracksUrl, { headers });
        const tracks = response.data.items;

        return tracks.map((track) => ({
            TrackName: track.name,
            TrackID: track.id,
            Artists: track.artists.map((artist) => `${artist.name} (ID: ${artist.id})`).join(' || '),
            Duration: track.duration_ms,
            DiscNumber: track.disc_number,
            PreviewUrl: track.preview_url || 'No preview available',
            TrackNumber: track.track_number,
        }));
    } catch (error) {
        console.error('Error fetching tracks for album:', error);
        return [];
    }

    // Thêm thời gian chờ sau mỗi request
    // await delay(1000);
};

// Fetch albums by artist ID and their tracks
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

        let albumData = [];

        for (const album of albums) {
            const albumImageUrl = album.images.map((img) => `${img.url} (size: ${img.height})`).join(' || ');
            const artists = album.artists.map((artist) => `${artist.name} (ID: ${artist.id})`).join(' || ');

            var alType = '';
            if (album.album_type === 'single') {
                alType = parseInt(album.total_tracks) > 1 ? 'EP' : 'single';
            } else alType = 'album';

            // Fetch tracks for this album
            const tracks = await getTracksByAlbumId(album.id, token);

            // Add album and tracks to the data
            tracks.forEach((track) => {
                albumData.push({
                    AlbumID: album.id,
                    Album: album.name,
                    ReleaseDate: album.release_date,
                    Artists: artists,
                    AlbumType: alType,
                    TotalTracks: album.total_tracks,
                    AlbumImage: albumImageUrl,

                    TrackID: track.TrackID,
                    TrackName: track.TrackName,
                    ArtistsName: track.Artists,
                    DiscNumber: track.DiscNumber,
                    TrackNumber: track.TrackNumber,
                    TrackDuration: track.Duration,
                    PreviewUrl: track.PreviewUrl,
                });
            });

            // Thêm thời gian chờ sau mỗi request
            await delay(1000);
        }

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

        for (const album of albums) {
            const albumImageUrl = album.images.length > 0 ? album.images[0].url : 'No image available';
            const artists = album.artists.map((artist) => `${artist.name} (ID: ${artist.id})`).join(' || ');

            var alType = '';
            if (album.album_type === 'single') {
                alType = parseInt(album.total_tracks) > 1 ? 'EP' : 'single';
            } else alType = 'album';

            // Fetch tracks for this album
            const tracks = await getTracksByAlbumId(album.id, token);

            // Add album and tracks to the data
            tracks.forEach((track) => {
                albumData.push({
                    AlbumID: album.id,
                    Album: album.name,
                    ReleaseDate: album.release_date,
                    Artists: artists,
                    AlbumType: alType,
                    TotalTracks: album.total_tracks,
                    AlbumImage: albumImageUrl,
                    TrackID: track.TrackID,
                    TrackName: track.TrackName,
                    TrackNumber: track.TrackNumber,
                    TrackDuration: track.Duration,
                    PreviewUrl: track.PreviewUrl,
                });
            });
            // Thêm thời gian chờ sau mỗi request
            await delay(1000);
        }

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

const readAlbumsFromExcel = (filePath) => {
    const workbook = XLSX.readFile(filePath);
    const sheetName = workbook.SheetNames[0]; // Assuming data is in the first sheet
    const sheet = workbook.Sheets[sheetName];
    const data = XLSX.utils.sheet_to_json(sheet);

    return data; // Returns an array of objects
};

const fetchArtistAlbums = async (filePath) => {
    try {
        const artistsExcel = readAlbumsFromExcel(filePath);

        const token = await getAccessToken();
        if (!token) return;

        for (const artistExcel of artistsExcel) {
            const artist = await searchArtist(artistExcel.Name, token);
            nameFolder = artist.name;

            if (artist && artist.id) {
                await getAlbumsByArtistId(artist.id, token, artist.name);
            } else {
                console.log('Artist not found or no ID available.');
            }
        }
    } catch (error) {
        console.error('Error fetching artist albums:', error);
    }
};

// Example usage
fetchArtistAlbums('D:/05-DUT/NAM4-KI1/PBL6/Crawl/Data-Artist/vietnamese_artists.xlsx'); // Replace with your file path
