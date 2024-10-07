import os
import unidecode
import re

# Danh sách định dạng âm thanh
audio_extensions = ['.mp3', '.wav', '.flac', '.aac', '.m4a']

# Hàm chuyển không dấu
def convert_to_non_accented(text):
    return unidecode.unidecode(text)

# Hàm lấy tên audio (xóa số thứ tự đầu)
# def get_song_name(song):
#     return re.sub(r'^/d+/s+', '', song)  # Loại bỏ số thứ tự ở đầu tên bài hát


def get_song_name(song):
    return song.split(" ", 1)[1]  

# Hàm xóa khoảng trắng
def remove_spaces(text):
    return text.replace(" ", "")  # Xóa khoảng trắng

# Đường dẫn tới thư mục gốc
parent_folder = 'D:/05-DUT/NAM4-KI1/PBL6/loc'  # Thay đổi thành đường dẫn đúng

# Hàm xử lý thư mục và tệp
def process_folder(folder_path):
    # Đổi tên thư mục
    original_folder_name = os.path.basename(folder_path)
    new_folder_name = remove_spaces(convert_to_non_accented(original_folder_name))
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
                print("loc:",item)
                print()
                song_name = get_song_name(item)
                print(song_name)
                new_song_name = remove_spaces(convert_to_non_accented(song_name))
                new_song_path = os.path.join(new_folder_path, new_song_name)

                # Đổi tên tệp nếu cần thiết
                if item_path != new_song_path:
                    os.rename(item_path, new_song_path)
                    print(f"Renamed file: {item_path} -> {new_song_path}")

# Bắt đầu xử lý từ thư mục gốc
for folder in os.listdir(parent_folder):
    folder_path = os.path.join(parent_folder, folder)
    if os.path.isdir(folder_path):
        process_folder(folder_path)
