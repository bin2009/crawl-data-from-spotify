import pandas as pd
import uuid

# Load artist information
artists = pd.read_csv('D:/DUT/NAM4-KI1/PBL6/CRAWL/crawl-data-from-spotify/Data-Artist/inf.csv')

# SQL INSERT template for the Artist table
insert_sql_artist = 'INSERT INTO "Artist" ("id", "name", "avatar", "bio", "followersCount", "createdAt", "updatedAt") VALUES\n'

# Prepare artist insert values and a mapping between id2 and id (UUID)
values_artist = []
artist_id_map = {}
for index3, row3 in artists.iterrows():
    artist_uuid = str(uuid.uuid4()) 
    artist_id2 = row3['Artist ID']
    name = row3[' Artist Name'].strip()
    # avatar = row3[' Images'].split('||')[1].split('(')[0].strip()
    images = row3[' Images'].split('||')
    if len(images) > 1:
        avatar = images[1].split('(')[0].strip()
    else:
        avatar = 'Unknown'
    bio = 'Null'
    followersCount = row3[' Follow']
    values_artist.append(f"('{artist_uuid}', '{name}', '{avatar}', '{bio}', '{followersCount}', NOW(), NOW())")
    
    # Store the mapping for use later
    artist_id_map[artist_id2] = artist_uuid



# Save the SQL queries to a file
sql_file_path = f'D:/DUT/NAM4-KI1/PBL6/CRAWL/crawl-data-from-spotify/SQL2/fullsql.sql'


insert_sql_artist += ",\n".join(values_artist) + ";"
with open(sql_file_path, 'w', encoding='utf-8') as file:
        file.write(insert_sql_artist)
        file.write("\n\n\n\n")


nameArtists = ['SonTungMTP', 'SOOBIN', 'PhanManhQuynh', 'NooPhuocThinh', 'HoangTon', 'HoangThuyLinh']

for nameArtist in nameArtists:
    # Load album and track data for the artist
    df = pd.read_csv(f'D:/DUT/NAM4-KI1/PBL6/CRAWL/crawl-data-from-spotify/Merge/{nameArtist}.csv')

    # SQL INSERT templates for Album, AlbumImage, Song, and ArtistSong tables
    insert_sql_album = 'INSERT INTO "Album" ("albumId",  "title", "releaseDate", "albumType", "createdAt", "updatedAt") VALUES\n'
    insert_sql_album_image = 'INSERT INTO "AlbumImage" ("albumImageId", "albumId", "image", "size", "createdAt", "updatedAt") VALUES\n'
    insert_sql_track = 'INSERT INTO "Song" ("id", "albumId", "title", "duration", "lyric", "filePathAudio", "privacy", "uploadUserId", "releaseDate", "createdAt", "updatedAt") VALUES\n'
    insert_sql_artist_song = 'INSERT INTO "ArtistSong" ("artistSongId", "songId", "artistId", "main", "createdAt", "updatedAt") VALUES\n'

    # Prepare insert values for albums, album images, tracks, and artist-song relationships
    values_album = []
    values_album_image = []
    values_track = []
    values_track_artist = []

    # Remove duplicate albums
    unique_album = df.drop_duplicates(subset=['AlbumID'])

    for index, row in unique_album.iterrows():
        # Album details----------------------------------------------------------
        albumId = str(uuid.uuid4()) 
        albumIdTemp = row['AlbumID']
        albumReleaseDate = row['ReleaseDate']
        if '-' not in albumReleaseDate:
            print(albumReleaseDate, type(albumReleaseDate))
            if str(albumReleaseDate) == str('0000'):
                # print("loc: ", albumReleaseDate)
                albumReleaseDate = '2000-01-01'
            else:
                albumReleaseDate = albumReleaseDate+'-01-01'
                print("convert: ", albumReleaseDate)


        values_album.append(f"('{albumId}', '{row['Album']}', '{albumReleaseDate}', '{row['AlbumType'].lower()}', NOW(), NOW())")

        # Album images-----------------------------------------------------------
        images = row['AlbumImage'].split('||')
        for img in images:
            if '(' in img:
                albumImageId = str(uuid.uuid4())
                img_url, img_size = img.split('(')
                img_url = img_url.strip()
                img_size = img_size.strip().split('size:')[1].strip().split(')')[0].strip()
                values_album_image.append(f"('{albumImageId}', '{albumId}',  '{img_url}', '{img_size}', NOW(), NOW())")
            else:
                # Handle case where image string does not contain '('
                albumImageId = str(uuid.uuid4())
                img_url = img.strip()
                img_size = 'Unknown'  # or any default value you prefer
                values_album_image.append(f"('{albumImageId}', '{albumId}',  '{img_url}', '{img_size}', NOW(), NOW())")

                
            # img_url, img_size = img.split('(')
            # img_url = img_url.strip()
            # img_size = img_size.strip().split('size:')[1].strip().split(')')[0].strip()
            # values_album_image.append(f"('{albumId}', '{img_url}', '{img_size}', NOW(), NOW())")

        # Tracks ----------------------------------------------------------------------------
        # Tracks associated with the current album
        tracks_in_album = df[df['AlbumID'] == albumIdTemp]
        for _, track in tracks_in_album.iterrows():
            trackId = str(uuid.uuid4())
            values_track.append(f"('{trackId}', '{albumId}', '{track['TrackName']}', '{track['TrackDuration']}', 'lyric', '{track['audio_path']}', FALSE, 'Null', '{albumReleaseDate}', NOW(), NOW())")

            # Associate track with artists
            # artistNames = track['ArtistsName'].split('||')
            artistNames = track['ArtistsName']
            if pd.isna(artistNames):
                continue  # Skip if ArtistsName is NaN
            artistNames = artistNames.split('||')

            # Handle artist-song relation based on artistNames length
            if len(artistNames) == 1:
                # Only one artist, set main to TRUE
                artistSongId = str(uuid.uuid4())
                artist_name = artistNames[0]
                artId2 = artist_name.split('(ID:')[1].split(')')[0].strip()
                artistId = artist_id_map.get(artId2, 'Unknown')  # Use artist_id_map to fetch the UUID
                values_track_artist.append(f"('{artistSongId}', '{trackId}', '{artistId}', TRUE, NOW(), NOW())")
            else:
                # Multiple artists, first one is main, others are not
                for i, artist in enumerate(artistNames):
                    artistSongId = str(uuid.uuid4())
                    artId2 = artist.split('(ID:')[1].split(')')[0].strip()
                    artistId = artist_id_map.get(artId2, 'Unknown')  # Fetch UUID from the map
                    main = 'TRUE' if i == 0 else 'FALSE'
                    values_track_artist.append(f"('{artistSongId}', '{trackId}', '{artistId}', {main}, NOW(), NOW())")

    # Combine values for SQL insert queries
    insert_sql_album += ",\n".join(values_album) + ";"
    insert_sql_album_image += ",\n".join(values_album_image) + ";"
    insert_sql_track += ",\n".join(values_track) + ";"
    insert_sql_artist_song += ",\n".join(values_track_artist) + ";"

    with open(sql_file_path, 'a', encoding='utf-8') as file:
        file.write("\n\n\n\n")
        file.write(f"--------------------{nameArtist}")
        file.write("\n\n\n\n")
        file.write(insert_sql_album)
        file.write("\n\n\n\n")
        file.write(insert_sql_album_image)
        file.write("\n\n\n\n")
        file.write(insert_sql_track)
        file.write("\n\n\n\n")
        file.write(insert_sql_artist_song)
        file.write("\n\n\n\n")

