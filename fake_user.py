import uuid
import bcrypt
import random
from datetime import datetime, timedelta

# Số vòng băm (tương tự saltRounds)
salt_rounds = 10

# Mật khẩu cần băm
password = 'password'.encode('utf-8')

# Tạo hash mật khẩu
hash_pass = bcrypt.hashpw(password, bcrypt.gensalt(salt_rounds)).decode('utf-8')

# Tạo câu lệnh SQL để chèn dữ liệu vào bảng User
insert_sql_user = 'INSERT INTO public."User" ("id", "role", "username", "email", "password", "secondPassword", "statusPassword", "name", "image", "accountType", "status", "createdAt", "updatedAt") VALUES\n'

# Tạo danh sách các giá trị để chèn vào bảng
values_user = []
for i in range(1, 101):
    user_id = str(uuid.uuid4())
    username = f'username{i}'
    email = f'user{i}@gmail.com'
    
    # Tạo giá trị createdAt ngẫu nhiên trong vòng 7 ngày qua
    created_at = datetime.now() - timedelta(days=random.randint(0, 7))
    created_at_str = created_at.strftime('%Y-%m-%d %H:%M:%S')
    
    values_user.append(f"('{user_id}', 'User', '{username}', '{email}', '{hash_pass}', 'Null', 'False', 'Null', 'Null', 'Free', 'true', '{created_at_str}', '{created_at_str}')")

# Kết hợp các giá trị vào câu lệnh SQL
insert_sql_user += ",\n".join(values_user) + ";"

# Ghi câu lệnh SQL vào file
sql_file_path = 'D:/DUT/NAM4-KI1/PBL6/CRAWL/crawl-data-from-spotify/SQL2/users_sql.sql'
with open(sql_file_path, 'w', encoding='utf-8') as file:
    file.write(insert_sql_user)

print(f"Câu lệnh SQL đã được ghi vào file: {sql_file_path}")