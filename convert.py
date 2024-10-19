import os
import unidecode
import re

# Danh sách định dạng âm thanh
audio_extensions = ['.mp3', '.wav', '.flac', '.aac', '.m4a']

def rename(name):
    cleaned_name = unidecode.unidecode(name)
    cleaned_name = name.replace(" ", "")
    cleaned_name = re.sub(r'[^a-zA-Z0-9\s]', '', cleaned_name)
    return cleaned_name

def get_song_name(song):
    parts = song.split(" ", 1)
    if len(parts) > 1 and parts[1]:
        return parts[1].strip()  # Loại bỏ khoảng trắng ở đầu và cuối chuỗi
    return song.strip()  # Trả về chuỗi đầu vào nếu không có khoảng trắng

def rename_song(name):
    cleaned_name = unidecode.unidecode(name)
    basename, dot, extension = cleaned_name.rpartition(".")

    cleaned_name = basename.replace(" ", "")
    cleaned_name = re.sub(r'[^a-zA-Z0-9\s]', '', cleaned_name)
    # print(a)
    return cleaned_name + dot + extension
    
    # print("1: ", parts[0])
    # print("2: ", parts[1])
    # print("3: ", parts[2])

# def get_song_name(song):
#     parts = song.split(" ", 1)
#     if len(parts) > 1 and parts[1]:
#         return parts[1].strip()  # Loại bỏ khoảng trắng ở đầu và cuối chuỗi
#     return song.strip()  # Trả về chuỗi đầu vào nếu không có khoảng trắng


# Đường dẫn tới thư mục gốc
parent_folder = 'D:/DUT/NAM4-KI1/PBL6/AUDIO'  # Thay đổi thành đường dẫn đúng

# Hàm xử lý thư mục và tệp
def process_folder(folder_path):
    # Đổi tên thư mục
    original_folder_name = os.path.basename(folder_path)
    new_folder_name = rename(original_folder_name)
    new_folder_path = os.path.join(os.path.dirname(folder_path), new_folder_name)

    if folder_path != new_folder_path:
        os.rename(folder_path, new_folder_path)
        print(f"Renamed folder: {folder_path} -> {new_folder_path}")

    # Lặp qua các thư mục và tệp trong thư mục hiện tại
    for item in os.listdir(new_folder_path):
        item_path = os.path.join(new_folder_path, item)
        if os.path.isdir(item_path):
            # Nếu là thư mục, gọi đệ quy để xử lý
            process_folder(item_path)
        else:
            # Nếu là tệp
            if any(item.endswith(ext) for ext in audio_extensions):
                # Xử lý tệp âm thanh
                # print("loc:",item)
                # print()
                song_name = get_song_name(item)
                # print(song_name)

                new_song_name = rename_song(song_name)
                # new_song_name = remove_spaces(convert_to_non_accented(song_name))
                new_song_path = os.path.join(new_folder_path, new_song_name)

                # Đổi tên tệp nếu cần thiết
                if item_path != new_song_path:
                    # os.rename(item_path, new_song_path)
                    # print(f"Renamed file: {item_path} -> {new_song_path}")

                    # Kiểm tra xem tệp mới đã tồn tại chưa
                    if not os.path.exists(new_song_path):
                        os.rename(item_path, new_song_path)
                        print(f"Renamed file: {item_path} -> {new_song_path}")
                    else:
                        print(f"File already exists, skipping: {new_song_path}")

# Bắt đầu xử lý từ thư mục gốc
for folder in os.listdir(parent_folder):
    folder_path = os.path.join(parent_folder, folder)
    if os.path.isdir(folder_path):
        process_folder(folder_path)
