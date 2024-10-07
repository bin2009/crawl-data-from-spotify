import os
import pandas as pd
import unicodedata
import unidecode

# Hàm để lấy tên bài hát (bỏ phần số thứ tự và đuôi file)
def get_song_name(song):
    # name_with_extension = song.split(" ", 1)[1]  # Lấy phần sau số thứ tự
    song_name = song.rsplit('.', 1)[0]  # Loại bỏ đuôi
    return song_name

def normalize_string(s):
    # Normalize Unicode characters, strip leading/trailing spaces, and convert to lowercase
    return unicodedata.normalize('NFKD', s).strip().lower()

def compare_string(str1, str2):
    normalized_str1 = normalize_string(str1)
    normalized_str2 = normalize_string(str2)
    
    if normalized_str1 == normalized_str2:
        return True
    
    return False

# Hàm chuyển không dấu và xóa khảong trắng
def convert_to_non_accented(text):
    text = unidecode.unidecode(text)
    return text.replace(" ", "")  # Xóa khoảng trắng
    

# Hàm để kiểm tra tên bài hát trong danh sách
def check_song_exists(song_name, audio_data):
    song_name = convert_to_non_accented(song_name)
    # print("++++", song_name)
    for audio in audio_data:
        # print("song_name", song_name)
        # print()
        # print(audio['name'])
        if compare_string(song_name, audio['name']):
            return audio
        # else:
            # print("----", audio['name'])
    return False  # Không tìm thấy



merge_file = pd.read_excel('D:/05-DUT/NAM4-KI1/PBL6/Crawl/merge.xlsx')
for index, row in merge_file.iterrows():
    # print(row['album'])
    # Đọc dữ liệu từ file CSV
    # print(row['album'])
    df1 = pd.read_csv(row['album'])
    df1['audio_path'] = None  # Tạo cột mới để lưu đường dẫn tệp âm thanh

    # Khai báo đường dẫn đến thư mục chứa các file âm thanh
    folder_path = row['audio']

    # Khai báo các đuôi file âm thanh và hình ảnh
    audio_extensions = ['.mp3', '.wav', '.flac', '.aac', '.m4a']
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

    # Sử dụng danh sách để lưu thông tin về tệp âm thanh
    list_path = []

    # Lấy thông tin bài hát theo folder artist
    try:
        i = 0
        albums = os.listdir(folder_path)
        for album in albums:
            album_path = folder_path + '/' + album
            if os.path.isdir(album_path):  
                audios = os.listdir(album_path) 

                for audio in audios:
                    if any(audio.endswith(ext) for ext in audio_extensions):
                        audio_name = get_song_name(audio)
                        audio_path = album_path + '/' + audio
                        list_path.append({'id': i,'name': audio_name, 'path': audio_path})  
                        i+=1
        # print("listpath")
        # print()
        # print(list_path)
        # print()
    except FileNotFoundError:
        print("Thư mục không tồn tại.")
    except PermissionError:
        print("Không có quyền truy cập thư mục.")
    
    # Lặp qua từng hàng trong DataFrame
    for index2, row2 in df1.iterrows():
        temp = check_song_exists(row2.TrackName, list_path) 
        # print(">>>>>", temp)
        if temp:
            df1.at[index2, 'audio_path'] = temp['path']  
            list_path = [x for x in list_path if x['id'] != temp['id']]
    # print(row['name'])
    df1.to_csv(row['name'], index=False)
    df1.head()
