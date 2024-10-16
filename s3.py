# from decouple import config
# import boto3
# from concurrent.futures import ThreadPoolExecutor, as_completed

# # Đọc thông tin xác thực từ tệp .env
# aws_access_key_id = config('AWS_ACCESS_KEY_ID')
# aws_secret_access_key = config('AWS_SECRET_ACCESS_KEY')
# region_name = config('REGION_NAME')
# endpoint_url = config('ENDPOINT_URL')
# bucket_name = config('BUCKET_NAME')
# prefix = config('PREFIX')

# # Thiết lập kết nối với DigitalOcean Spaces
# session = boto3.session.Session()
# client = session.client('s3', 
#                         region_name=region_name,
#                         endpoint_url=endpoint_url,
#                         aws_access_key_id=aws_access_key_id,
#                         aws_secret_access_key=aws_secret_access_key)

# # Lấy danh sách các tệp trong không gian
# response = client.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

# def update_file_content_type(key):
#     try:
#         # Kiểm tra phần mở rộng của tệp
#         if key.endswith('.m4a'):
#             # Cập nhật Content-Type nếu là tệp audio
#             client.copy_object(
#                 Bucket=bucket_name,
#                 CopySource=f'{bucket_name}/{key}',
#                 Key=key,
#                 MetadataDirective='REPLACE',
#                 ContentType='audio/x-m4a'  # Thay đổi loại nội dung thành audio/m4a
#             )

#             # Đặt lại quyền truy cập thành public
#             client.put_object_acl(ACL='public-read', Bucket=bucket_name, Key=key)

#             return f"Updated Content-Type and permissions: {key}"
#         else:
#             return f"Skipped (not an audio file): {key}"
#     except Exception as e:
#         return f"Error updating {key}: {e}"

# # Sử dụng ThreadPoolExecutor để cập nhật song song
# with ThreadPoolExecutor(max_workers=30) as executor:  # Điều chỉnh max_workers theo nhu cầu
#     futures = [executor.submit(update_file_content_type, obj['Key']) for obj in response.get('Contents', [])]
    
#     for future in as_completed(futures):
#         print(future.result())
