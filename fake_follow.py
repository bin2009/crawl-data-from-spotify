import uuid
import random
from datetime import datetime, timedelta

# Danh sách userId
user_ids = [
	"6a73b3d7-a5f4-4345-85fb-444952459fc1",
	"c66c86cc-5f3c-4f05-ae4c-90ca86047e7f",
	"4e609f07-2909-4222-a99e-27276633530e",
	"58862df5-97f2-4d63-9c72-8f7e136c747e",
	"aa164380-9d8f-4efe-a340-e4d414616eb4",
	"16a1c313-c40d-4623-895a-8a910283e631",
	"b3643f92-95ef-4d79-b51d-d11ae4ea1d98",
	"8ec2bb70-df3f-4111-af23-c4f29c93c02d",
	"c4993a24-7549-4660-85cb-da4044e8e40d",
	"393aafbc-a90a-4924-ac81-ce1699a45da1",
	"57cae432-d9df-4903-a033-7cf060f3e6ca",
	"cf2406ac-2a91-4987-b91c-5bf45fd356aa",
	"d60f75c6-f0c3-42c2-a850-293c74a90e45",
	"963f9082-b73b-4716-ae79-86f09672d09a",
	"2872fcd5-a69a-4118-a5a4-f50cf9f6df46",
	"bc6b7cb1-8244-4d40-86bd-f04d88d263a4",
	"50cb0b2c-30c3-49f3-ac20-fc5aaef908fc",
	"30e1328b-f5c5-4c5b-afac-6bccb81182c0",
	"ac89a6af-d4ce-49b3-a6c7-63939ca0d924",
	"b8fed1e6-279b-4de0-a1c0-b8ec845189a3",
	"872059b1-fc0b-4398-86c0-09d4743ea3b0",
	"fc842ffd-ab6f-479a-95a7-1eaac3376db8",
	"3c890e68-ca74-4d58-b731-1661e1f5afbf",
	"488eaa7e-97f4-4e4a-9657-7de85c5c72ac",
	"a5754872-5fcc-40e2-85e9-2f04bf8ee085",
	"99a9309d-4d56-4fce-b917-2a5a97c11b65",
	"330acc8b-ec34-49a3-828d-dfb68cdc820e",
	"82f1b23a-4498-4146-9b25-e83a084ae82d",
	"00647a5c-64fe-42cd-8ee1-de0327d25edc",
	"e9e1f50b-d277-43a8-9a87-23de70925e81",
	"9adeaffc-e50f-44a1-a31f-7f51ad77706b",
	"5e3689fd-c988-4183-b7b7-cc8b849c9491",
	"20045a8a-ae9d-49b6-99ad-7961f5ea4805",
	"e1374338-1bcb-4a33-8c08-a2659b94f932",
	"5f05bfc5-b50d-4505-becb-300f8a6e2ea1",
	"01a11b8b-bba6-4684-8304-1a10ae8d14e2",
	"1e85bcf7-a3f1-484c-9ef8-b16fa50e09d0",
	"93c09554-aca7-47aa-a279-622c2367beb0",
	"f913069e-24ff-40f9-8a0c-715617641b00",
	"8c2f3b8e-64b5-474e-b045-ae0790a43dd3",
	"ea70afc2-aed4-47b6-9789-0ddf9614aea0",
	"e9d9641a-1f91-4b72-8d08-80ee512fa03e",
	"e6e672d1-7529-4ff6-b802-7c60fe358826",
	"9ff6021f-8de0-473f-b870-760624b2f5dc",
	"d8addd07-11f3-424c-a1ce-e9b0dba99bc9",
	"5dd4260d-eb8a-4cf8-bcab-85f760405d9c",
	"f7a111ee-cf3b-4c26-8c96-85d117447bfd",
	"16b8b77a-8a2a-4ae1-9130-5c02559c6314",
	"95eb0aa5-4d4e-4385-88df-6a05b0d5a736",
	"cf280f65-1720-429e-9670-2881dd8d10e0",
	"b888d01c-0ea8-48fd-ab33-ccaa47038036",
	"09fb962b-8881-43cc-b8a3-6f4faa1809a7",
	"7695de84-1cdc-416f-b0b7-2c64ca8b1eb7",
	"87d87534-45c1-497f-991a-16cefd44aab8",
	"1a31da6b-a394-40ee-8015-856364841c9e",
	"3d90a73f-fac6-42d8-ba81-eb515e461e1b",
	"95736875-2913-410b-a6ab-b9faa90ca56d",
	"79a8f832-6350-4fac-b4e8-290e926d08c7",
	"15eb0294-088d-4af0-9b61-7a52ad9b68bc",
	"c0156276-2a93-489d-986d-8d5d0d2a2692",
	"5b14bedc-7682-496e-9ecb-3e1ea11dc102",
	"337a32d3-fc91-4e0e-861f-15721bf7425a",
	"db5a92fe-7905-48c0-8c92-acde48a1667c",
	"7296909b-7c19-4018-99e3-add932e62c06",
	"cf0aeb6d-e60d-463a-ba62-acaefc0ddec3",
	"21073808-ea04-4cab-8212-28d697880eea",
	"42f20991-996a-4a91-acdc-d040c7a26fc3",
	"43b9b30b-0be0-4351-8af6-def7705d9165",
	"edafbe6c-a2da-4366-a458-f72f92377aad",
	"151c858b-7b48-4600-8a17-10215e53eaeb",
	"11e56660-9bd6-4494-9f5c-102a96ea4b81",
	"f7a32320-0ff7-471b-9530-7b12ec900ebe",
	"2ad611c2-a828-4123-8d7e-747516a6a3fa",
	"d7b8bdf4-00c8-493c-8735-67b9207d4b70",
	"47ce3ddf-0967-46bc-85e3-3d22a853e6f1",
	"c8880db5-c113-4a74-af9e-3493ffda8ff4",
	"9a4c6d52-b710-442f-a633-cf570bdfbe97",
	"fcfe8278-fb2f-4b46-88bc-3b4d4c6cbbde",
	"9027682e-8458-492f-85b0-e5bf878a637e",
	"a2ba290f-b544-4292-8592-d2835b831116",
	"fb5f35a3-8bf7-48b4-a81a-0f678383207a",
	"94fdea40-d941-47fa-8faf-8c8781ab51fb",
	"d1068773-7efa-4575-9f0a-d03c15fe58ce",
	"c4f4a02c-97f9-463b-8d0c-023f1cc8de7f",
	"b886300b-edb0-4b70-a43a-feeb59e95fc5",
	"5af25344-5fa7-4c61-8181-d75b3dfd7424",
	"39c76575-73ed-4130-917b-00380dc0c006",
	"e40757a9-1674-49a9-b021-34babaddaafb",
	"72a7cfa9-ff7c-4973-ba2c-e8a08d412218",
	"60351be7-98f1-49a7-9fd2-4d0a0ed564e3",
	"222f21f3-5b3d-482e-8fe2-8d2b2658297a",
	"20f84605-1ce6-4f79-8b59-8c7932851ef7",
	"9e306496-2449-459c-b045-20beaf2b63f5",
	"6e638f04-4cb7-4f10-972f-84d89b6fa22a",
	"5f51da3c-3583-4064-87c2-ea1c00837918",
	"dd39bdc5-7934-4cf9-ab28-560e3f7f2c72",
	"b3aa0177-8eca-46c2-8a13-92c1f8cf1013",
	"d9e39fe0-3b76-4b96-b71b-61e36b6f604b",
	"7fe0868e-6259-428f-9f3d-b07ec5646804",
	"00e22dc1-dbc7-473b-be84-aaa2f2abcce8",
	"88aadb4c-672b-479a-b62b-67f26a3fdce8",

]

# Danh sách artistId
artist_ids = [
    "f71bf4e2-64ac-4996-9efc-25e85f02744c",
    "92bee438-2de2-49b6-8ee4-31404bbcfd08",
    "ef10f526-25ef-4e6f-b65f-82f812b43f79",
    "b3fcc66e-1dd6-4ef3-80c4-fea8993a08d2",
    "16038760-3447-4d49-a8e5-ebc642aeed9a",
    "09acb49d-eb2f-4728-b0d6-1681f57ae6f3",
    "fd3b42ad-31b9-4615-aff7-0fd3ac9f4a0a",
    "e2dd53c4-55f5-4df6-a098-8a93b964e6ee",
    "cc2961cf-0f5e-40ea-aedc-c2fabc3ae22c",
    "92e33f17-1775-480f-a061-7129ab55ea84",
    "bcc0be1f-b6e1-4995-ae88-135b1539d312",
    "c93954af-f56f-4e08-adb4-703c7a398977",
    "683ec6aa-6a33-40fc-b371-d5c2261d3795",
    "fe2c594d-466e-4cd5-8440-fd990df291d7",
    "dbe9f05d-a111-4846-9c98-1bb53377f348",
    "1b85e232-2e14-484f-8195-78ed56226d8b",
    "81ff3dc1-9b26-4d4c-a40a-b15923b8d426",
    "5e879adf-1bdb-45b9-aff5-73c9a8c24f50",
    "a605e208-26ae-44e4-bc8e-e4b39fda5f08",
    "427b3271-8296-4855-b673-975e9767ed46",
    "5a866865-247e-4bcb-a6f2-22e73e62916d",
    "637ee305-dd52-4499-bc36-cf7418b637b8",
    "3a1efe6e-d651-4479-99a8-2141391eaf4b",
    "a046df20-aa6a-45a9-9127-14b65d95270a",
    "2658c114-6dac-44ce-abd0-88e80c45091d",
    "f42cb745-d0f3-4728-8c49-5a5839943fbe",
    "e8db0fd9-9b10-43a3-902e-58f5c6d6abe6",
    "62d5ae5b-ad3e-4954-b93f-b968d2997f75",
    "1169429a-35d5-48a0-b20e-1faf6f3dd029",
    "9faeb18e-9202-4358-a64b-c44d5a04ae58",
    "9b55e52b-3613-4f2e-9ea2-aaf09df60fe0",
    "f96cbf56-2488-41de-8953-cb529be9ed98",
    "f20e697f-5e98-46e8-8e67-e23f5a542d32",
    "92dc1c37-9232-450c-9f26-f2e15653eb67",
    "6c1c8d3b-bb2d-4251-a43f-1be005f368d1",
    "ee64e40c-4656-46b4-8b07-f79f865e321e",
    "6359ffd5-2606-4641-8d7d-da80f489bd1d",
    "7315f681-c14a-4dd3-8c21-cb81c824eb84",
    "d2a0e3cd-35fa-40d7-8edc-fd74bc5c64c6",
    "37030ccf-7406-4aa5-9dc8-2f0a21003b76",
    "69e338a4-a08c-4d2e-a07c-73ea7100d826",
    "cc5622b3-bdff-4614-ad77-5fc370599b1b",
    "d1c2ac78-dbd4-4d40-ba91-851d76920ffa",
    "aa3b6b26-def3-455a-b9ea-37f572f067cd",
    "52786d31-eaeb-443d-8600-78ef8735e2c3",
    "e2b51e04-1ff8-4238-a4be-6f6ffc93079d",
    "2c77a689-15f1-461c-8c5b-8629d2643017",
    "391f3a9b-f4b7-4c1a-8af5-5f1650a41013",
    "17ffca0a-4965-4964-8865-46a03ab3ba05",
    "bb4645d3-46ea-41ac-b282-1306d149703c",
    "cb8d373d-c2b6-4b76-9404-1bfcd72f80b7",
    "42c013d5-9b25-4753-976f-72f8a4839403",
    "6cc51e68-1279-464a-a763-d53174d217b6",
    "776dc8d3-5ab8-4adf-9ed4-4242b24e7e16",
    "8dd32c48-18c7-438f-905f-63d2f90f0b72",
    "ddcdff27-b171-4808-8e64-24b45e5f8f69",
    "9a143867-2456-4e55-83d2-e6738c785a38",
    "77d32a28-c822-4d8e-a361-61ad91477ff3",
    "6552329e-f2f2-49ea-a0cb-43bebf4dadf6",
    "c4ce5d0c-eb39-4058-9cbb-81fcdf520403",
    "d3307df4-8e92-4b6d-9833-2faf9daa4f19",
    "d742c0a0-6473-4592-b87b-343e16e19ae7",
    "7ef0c523-34f1-44aa-a143-ef9e30bd96f1",
    "072ec035-cb35-4d04-a8a1-6bbcdb7b5682",
    "59027145-2234-4792-b593-b404dcc2b6a4",
    "8a1c5c0e-1ea2-4391-88a2-e5998dc4a540",
    "99372c4d-cf3b-48cf-a8a7-023ad238413d",
    "175a5187-7f3b-41ec-95b5-78488cd2ee4d",
    "386d1a7d-a6ed-494e-93fe-87b6de90d0f4",
    "d3828a73-e50a-4382-b57c-0501ec2c0793",
    "1058c12e-8a7b-46c5-8ca8-5ee12fc2500d",
    "fb0cc934-b1ae-4752-8485-821fa051b77f",
    "b7c9337a-d695-4aba-8283-5e22c85354f8",
    "75025988-f737-4c0a-b04a-04cfe9d921d6"
]

# Tạo câu lệnh SQL để chèn dữ liệu vào bảng Follow
insert_sql_follow = 'INSERT INTO public."Follow" ("followerId", "userId", "artistId", "createdAt", "updatedAt") VALUES\n'

# Tạo danh sách các giá trị để chèn vào bảng
values_follow = []
num_follows = 3  # Số lượng nghệ sĩ mà mỗi user sẽ follow
for user_id in user_ids:
    followed_artists = set()  # Sử dụng set để tránh trùng lặp nghệ sĩ
    for _ in range(num_follows):
        while True:
            artist_id = random.choice(artist_ids)
            if artist_id not in followed_artists:
                followed_artists.add(artist_id)
                break
        
        follow_id = str(uuid.uuid4())
        
        # Tạo giá trị createdAt ngẫu nhiên trong vòng 7 ngày qua
        created_at = datetime.now() - timedelta(days=random.randint(0, 7))
        created_at_str = created_at.strftime('%Y-%m-%d %H:%M:%S')
        
        values_follow.append(f"('{follow_id}', '{user_id}', '{artist_id}', '{created_at_str}', '{created_at_str}')")

# Kết hợp các giá trị vào câu lệnh SQL
insert_sql_follow += ",\n".join(values_follow) + ";"

# Ghi câu lệnh SQL vào file
sql_file_path = 'D:/DUT/NAM4-KI1/PBL6/CRAWL/crawl-data-from-spotify/SQL2/follows_sql.sql'
with open(sql_file_path, 'w', encoding='utf-8') as file:
    file.write(insert_sql_follow)

print(f"Câu lệnh SQL đã được ghi vào file: {sql_file_path}")