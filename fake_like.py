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

# Danh sách songId
song_ids = [
	
	"5835e4d4-02a8-44fd-81ad-75aa79cd944f",
	"9c84b01e-4f52-45eb-819b-dae27c19b00b",
	"aff154f8-a36c-4b96-8d14-ed03e5e2be92",
	"79e25b3d-b06e-4abb-84f9-847282e083f5",
	"d298e699-e853-4aa8-81be-1a8b412a2516",
	"ca6d3c94-0410-4f91-a56f-3236713db314",
	"327f2d81-a337-4934-af40-7cd86870ff41",
	"6f6e1c83-9934-408c-bb69-78eac97ce339",
	"13de03ba-87fe-45e3-a38f-9654823ec4fa",
	"7cad90fe-d6ca-449f-b27b-db6db9c9c50c",
	"946ebadb-8904-4599-b8a0-56a02eabc0ab",
	"c481f2e8-9bc5-4748-816c-ed3f9f11ec7d",
	"510f21e4-b84e-415d-8399-b5ab62bd5c7d",
	"68fa5a97-88a7-4b9c-a098-6295bee53f01",
	"bdd18db8-09c4-4094-8002-0cb7f1c16585",
	"108b042d-558a-4a7f-bacb-01b650fa814b",
	"2aef1922-2fe4-4a46-a5e2-f91972258029",
	"cfe3a7fb-30e7-41ea-9868-54cf3abe86c5",
	"f087cfb1-5b4f-4451-8720-7dc9c757068c",
	"cb82252a-fb36-45bb-b568-c16675de6450",
	"d9801843-527d-403c-a045-865c134030c8",
	"b09c0fa5-6f30-4bec-811e-557e12de73cf",
	"2ba1d6a7-f419-4f71-842e-bd057b63be55",
	"6befc70f-5b72-4087-aec5-dfb7a9cd6891",
	"4683055b-eafa-4de9-a49d-687f97c3fc05",
	"fb657ef6-f76c-44f1-9b6c-94e4ccc78e11",
	"0bd1b44b-7861-41b0-a9f1-7b6fb3accf25",
	"3af11300-c88e-4a4f-838f-386c41938a89",
	"e90a0a74-1448-48a6-b54e-1c478cfefe48",
	"8c9ff7eb-31b2-461b-8d35-56ea82c67315",
	"ba25089d-de2f-4519-b6bd-2d6ea8e8bcfb",
	"9d77b911-7a29-431f-a30e-057fceb46980",
	"6933d5aa-a1c9-4527-86f3-2ecf6e406d58",
	"3d627c8f-aa6c-4231-a4ba-23883a20bb8b",
	"edbbb012-b85a-49aa-a26e-5d5a2e37bf23",
	"e8a6c579-ceb7-4805-b0ac-74d129cb2a92",
	"389c2e82-6eaa-4df1-998c-2eb560dd798f",
	"655d6efa-fce3-4c6a-be0c-be94c610b6dd",
	"a0105bc1-f054-45b8-851e-f3a40a6d4e33",
	"bc7985f4-3a8f-4fd2-a58f-bf3d6ec97dd0",
	"5491bdcd-e167-4e29-9847-0e06462600d4",
	"d38dbc2e-1ed1-4eb9-ae4f-67b0bb1c1615",
	"e505049a-02d6-4b84-80bf-75d25a87f93a",
	"393da71d-e6fd-498d-ae74-4e3c4589f132",
	"b351447f-29b0-4d82-bccd-834c009014eb",
	"2500c7f0-5be4-4604-b3fe-d5dadbc8b0ba",
	"befff4dc-707b-4ff8-8669-447633285955",
	"50197de6-d920-4b09-95a4-86f0c9cf43fb",
	"3ac35a41-6a31-4e0e-97eb-c6323eff7a0f",
	"39fc20be-940e-47bf-802a-bf6ee41b9589",
	"8864ca57-94a6-4be8-9a98-69ba23a57213",
	"f66c7de7-01d6-440b-b538-340e32784517",
	"adb67765-82f8-4a6e-9ab3-c2369b1558b8",
	"29277cc9-dd79-41ac-99db-e0d28dc553a5",
	"7198569d-743b-4d82-80c2-8a72f27ad554",
	"f1e780ca-b507-4e5e-882a-7f716d23e4c4",
	"a04a6592-126f-4408-b9a3-d78b5cbf23cc",
	"d3677691-1be5-4960-b3e9-518d352abde1",
	"863e6314-15c1-41f6-8c87-87a533f080d9",
	"1bfadd5e-8eb8-415c-8735-51cfb050bb01",
	"cffaa8bb-e121-4ca7-a846-35b1a3145c32",
	"9466ddd8-6a86-49b2-a8de-71790bd0cd4f",
	"d09c33cf-1c23-446d-ba74-90f972d1ffcc",
	"ceabda57-321e-42fd-8af2-138ad7d00b59",
	"d5de051a-6e76-4e4e-8b34-8e070812453a",
	"127f9b69-724f-4b10-9c45-7866aba6a09a",
	"3ebbcd4b-c4c8-48df-bc4e-ce890469b307",
	"32f9a00c-bd34-4646-919c-026353b06f31",
	"2149c07b-ed71-433e-8caf-6f60a5824ad0",
	"88394cf1-3447-4e7d-9522-773d84e784da",
	"b1045454-a374-451e-a3f5-2b587525298a",
	"6e892e1f-92a5-424e-9003-6382d56db2d8",
	"dbe941f4-ed7d-4fb4-afe7-15e3ad23f026",
	"671d1430-b688-4f83-8218-651216a0d570",
	"22068ada-55cf-4ca7-80cb-6c325612fcf8",
	"d4e81194-3865-4509-ae5a-75a23e20c949",
	"92a7bd6f-ce92-4209-b30b-7696f2f6e3b0",
	"2c242553-fca4-4f4c-8fc0-5d58c9b7ac01",
	"0f03cd8d-bdee-4a72-b78f-bd475f1d586c",
	"825a5f8c-4827-4f5e-a9b6-06578f0105c2",
	"c47879e5-e3aa-46fc-b246-b98885d912d5",
	"548868f3-4eca-4efe-9ea3-ff46ec065d0c",
	"ddb5e26b-f1cd-49f4-a4e9-b155a0c64c85",
	"1a340435-7801-4f7b-837a-5046542f2cea",
	"029872df-4d98-4bf7-96bc-746657362af0",
	"3817ed80-684b-4ea3-99f7-32a543f58a0a",
	"a8a64d7b-120b-46c6-8182-a77b22b637bb",
	"eb5e9085-75ae-4626-8a25-f32ffc4fa235",
	"103c07e2-4ee0-4b64-aab6-1617b5b22eab",
	"93ef83f6-775e-45e4-b29d-e11712d6f3bb",
	"43be9aac-88dc-458c-b18a-1d101f09a9d1",
	"810c92ac-9441-4ec4-8720-9e0226c8447c",
	"097b9866-8c2f-471a-bd48-8ea3566ad9d3",
	"e0729ee0-b54d-4acb-9e7d-5c2b8a63ebc9",
	"0ddeada6-6e72-47db-8b3b-82a3bfc5e255",
	"5719542a-6385-4f2e-a0fb-e68bcc9315e2",
	"f6e68e7d-b2aa-4a26-b15a-0c0e0d975f4a",
	"ba1e23eb-feac-4258-9642-19e328386172",
	"3b9bfc48-b49e-4fe9-b39f-88e3d45d52e6",
	"5dda2490-3a18-4967-a54c-69804732ad38",
	"3a3712b4-20c4-4831-b3a9-127bb31ed4f5",
	"1aeb50bb-3866-4ed0-8125-7981e160f5ec",
	"c6e83895-117e-46f5-978e-3638869776fd",
	"a5ad0fc2-d19f-48cc-8a41-4e685bc9c00b",
	"e6e986cf-684e-41bc-b596-06675f3931af",
	"ef4c6f0f-9294-423c-a16a-ee176e45f789",
	"5aab18e9-962c-4988-8202-3d98b2f1c96f",
	"ac8b59bd-74f1-4431-9f25-2b9eb7444ed6",
	"87bb5ab9-3842-43fd-9f3e-95b1c14bbbb9",
	"1f99fd72-2938-4ff2-aefc-2c2567de4e41",
	"025f131a-eb75-440f-9f71-a35320f20040",
	"9d7d2425-80a5-4873-8b88-e38240fbf7d4",
	"7eedafbf-6055-4f86-b1e5-65b193b0e3ea",
	"02a86fdb-ec01-4e9e-8bbe-88f92f9acff6",
	"45eaa563-4204-4e57-90c9-7dd942fed247",
	"f790a38d-807b-494f-ae69-f72430af8feb",
	"96393c46-88d3-470b-b04a-36f4783c85a9",
	"dda6a00a-cdc6-403b-b893-7206cacabda8",
	"2553cc00-78ac-4800-865a-dc17432f9098",
	"f1ac70b9-2116-4ae7-b374-5a219550b6f2",
	"c39065b8-6e48-4cd1-9f22-7a160a63a292",
	"1a5df7a4-c148-4f86-87f1-454ee88822ee",
	"0c244652-d9c4-4045-a3fe-f3c2ed52ea47",
	"05875d22-a1fc-4f66-9af6-94bcb8c267d7",
	"30215bf3-0ce9-4a6e-844b-41538d0ec037",
	"36de57ec-7745-4a31-a480-79cf8dac465b",
	"c7a4093a-8c7b-4b8b-abd1-ac74c30e9215",
	"a0317a3c-9eff-4f4e-87d9-c520c8bba820",
	"847391a6-e3bb-4844-a690-2578e8d906cb",
	"4879c136-b428-45fa-93d2-69cb6423df9a",
	"aa84a455-39af-46e4-82d1-4b012292eb16",
	"ef99a421-811e-4d08-9c9b-9f16c775598e",
	"11859001-a578-4fa1-9673-2c180906110f",
	"b05456f6-364c-49cc-b99d-ddffb25ad7a8",
	"94f684fd-640b-4d22-8e1d-466bb321ff7d",
	"3de1e75a-d214-450e-9139-3f3f2ebd1e9e",
	"a57650dd-7981-4895-a0e6-788292681998",
	"30a3e6a6-97e0-46cd-8397-196fbe95981e",
	"f91697eb-4168-4148-ba06-dd5c20bbce8f",
	"2b82bf84-3eb0-4d7f-8093-2e3cfaa7e801",
	"01fd6346-832f-4f77-a32a-6b5b5a20ebf4",
	"65138124-1d86-4647-acba-bf61edf3ee6c",
	"19681058-4330-4ddb-8194-76b95adecf1e",
	"7c0c4c1d-e1ab-4678-995d-ece816c9ad75",
	"58e4ce38-de30-4b18-bb87-27f2ff90ac51",
	"ddace5af-f526-4db6-96c0-ef402714ed9c",
	"143e6525-4a38-4707-98fa-eb7421dcf334",
	"48539223-f697-424d-a0c2-9039777db987",
	"63371197-33fb-446c-89fa-152eaa7bdbae",
	"9b99580e-e22e-4c40-8510-b69480dd7668",
	"fe3178a5-9fdc-4f94-a46a-83ba5d03d76a",
	"85e32e2b-2cb6-4000-9791-c0f5df067d73",
	"28d5aedd-f6c5-4283-8d02-95a9e00b5b15",
	"410a1bbc-5ca9-41c4-9857-7de99d14a678",
	"c12a1703-9759-4f37-ac09-69f5f444dea7",
	"0ec998e2-cb42-42b7-8287-69a38d8df773",
	"c6fb24ab-84b4-432f-a47b-50bf192b5aaf",
	"8d4a10ae-9b8a-4d2d-bec2-d777057fe2b9",
	"aae2aac3-9293-4605-9411-d4ddb63b7462",
	"56d5523f-e933-441c-ba90-d4714dbf2fde",
	"1d07e0d1-681f-4959-9191-6a26cdca70ee",
	"60efd7c1-df46-465e-bb7b-4b026f8a9bf4",
	"b012e4a2-2ed4-4002-a24d-4bfd6684f45e",
	"d604b833-7cd2-4c8f-9d20-ab3cef65ab42",
	"64035189-964c-4d3d-bbb7-e17d1a07d28c",
	"e37bf502-788b-413a-990a-c0b5b0dca2d5",
	"827a2bee-810d-406a-a451-77440605d7f9",
	"6853737e-cc1c-4d51-aab0-c4c9d8a145ec",
	"08db298b-5514-4214-8592-4f6cbdc8d21c",
	"dbc9691b-1503-4233-8beb-c49acdc7e432",
	"29b7b167-7a30-4383-9f2b-6cd9a7954e62",
	"04cb9d01-ac20-4ddd-97c8-0795cd58fc82",
	"e6413041-c041-4deb-a07d-4d957130caa7",
	"32a4d2fe-0d98-4ab9-9a23-210d36c8e3ba",
	"2cd1cf26-e770-4a5f-805a-97b4afec4c42",
	"34d2c826-cef0-4353-8bf3-d66d03373c6b",
	"4af47e26-58c0-4bd2-ab8d-78be9673d432",
	"ca6604a6-651d-4351-a01e-22b15232f514",
	"850b1990-1e03-40b0-89a1-fd025c16cc36",
	"c03bbb1e-01e9-4e03-a577-fa372e986070",
	"d63706fd-4d67-414d-b4d7-93f7deab15d6",
	"a977c234-494a-4dd3-bd5a-e1ab4c825838",
	"1fe1fa28-f9b2-496e-95b9-aaa58669544d",
	"f6e7edaa-a17f-45c7-a45f-2303a31f771e",
	"3f400b98-767a-4b98-86a5-160d0ed9f0e3",
	"9781d08c-3e0b-4f37-bcec-d5c524d1b7ee",
	"ff4942f0-eb25-4c49-af67-3cca068aaf45",
	"ffd96b43-b1a7-4fa4-ab82-0c210238e37f",
	"062bd1f9-3e49-4d3e-b67b-5561cb2989ac",
	"3ce05d6a-b930-4642-b420-98ead746e36d",
	"7b830026-9803-4177-8cbf-e52b1e916a2a",
	"17b1da55-f0e7-4f55-b80c-350aff7e0d26",
	"1765dc42-b65a-4915-965a-85ecaa90085f",
	"9d047c02-bd5a-4dde-8764-ab4b60ce2796",
	"1cbf55ec-9ae3-477c-9ea0-01d6b35e36aa",
	"435dfb9a-16f0-409c-a54a-eab74902e3e8",
	"11912d9f-8417-4a50-8cd8-e7ca3e525805",
	"b6bc57f3-9d9b-488b-95ca-bb2f7fc94461",
	"16fc77d0-00c6-40bd-898f-f37e5e0b0f80",
	"57791051-8b18-4ff4-b967-347db541ecf7",
	"748237b5-c1c8-463b-b658-a2bc9830281a",
	"fcb55dc3-4968-4293-9692-a9de05a6c9b1",
	"2aa58407-4cbf-4cb8-9ad6-2dfbdfac1457",
	"c9b3c755-c7c2-4b20-8f68-5d0035674308",
	"c8b73c5f-9fcf-4f94-b006-ed3ead9787e7",
	"110efe93-bf3c-45d9-9fd5-f68801f7f351",
	"c37571fe-6f8d-45b5-b39c-6e5a6886fcef",
	"5302e6ec-bef6-4056-9c21-3ffb90632cdc",
	"6ebddb22-d867-4139-a237-c32416ac878d",
	"189fe61b-608c-4c61-a2d4-9720728b0010",
	"5a78fbfd-ed3c-4df6-90c8-890f93d11bdf",
	"3eec1c88-241a-4e39-a3b9-b948b5d55771",
	"0abac169-e59e-4da7-b225-dda8a24b569c",
	"7e16f4da-9ce6-4b3f-b382-7abe583b211e",
	"a93f4f03-7bf0-46e2-84cd-5bfd423dcaa8",
	"32cb81a8-202f-4f26-a854-da057cf8bb9e",
	"8be35ea6-4fb5-47f4-9118-e54938deb787",
	"79950119-c261-4dc4-b0a4-fa12c63db8ae",
	"31c5ec0d-0d42-41e4-98f5-4bee83ed5b35",
	"9b416203-2274-41c6-afc7-a662160d96b8",
	"0e5f0889-1ed9-430f-8a04-f69bdd63f0d0",
	"5582b880-3748-4f8f-b2b7-1b5b175c18aa",
	"a623cce9-0a09-4f09-a10d-ccc2720e9e62",
	"06952bfa-343e-4448-83e2-32a7968f878f",
	"8cfaf269-ac82-4da7-aae8-74d98d13c252",
	"9cba8c9b-4c3b-4fe8-a5da-3013cb701f82",
	"e40e5014-d3e5-4960-8018-0cad8af5eea1",
	"ffe05160-b6f3-4570-9252-6d1e98d6ebda",
	"6b4cad99-b9ce-4799-8239-5de4c6996ffa",
	"6c0a23fa-e643-4920-947e-2c321c9838bb",
	"10336aae-3594-4fb9-a883-44c51a50cd26",
	"84718b25-d8f9-42cd-8ea1-6faafcb33c59",
	"dc2f22f9-5442-4be7-a108-bb05563dadd0",
	"6be7446d-7641-4fd7-9c76-b197c26cd128",
	"6927691d-b1e7-4512-9f68-f76258138676",
	"50c0b9e3-13bc-4d84-b460-e41c6570f397",
	"781fb9ea-ff57-49ad-b349-34616fb65a49",
	"241983a3-fc6d-4515-8cbf-ab8800aa34f3",
	"77355f35-32e9-40ed-a38e-9e09efa16ba0",
	"f21e2ac3-e50b-4b98-89e1-aef87a71888b",
	"25266697-2b08-4ebc-a432-6f07b3dc833e",
	"d054d0a5-8e12-409f-a072-de3aef831b87",
	"7b62b5a8-89a6-43ff-bc97-ca7c8b14f3af",
	"0432654e-da50-4917-8b80-9129103f4f69",
	"7d8fb632-2386-4290-83b0-4357b5ed472a",
	"43b4bd1a-88c7-4221-bbd8-ae8d9a5ea884",
	"d79b83fb-8d11-40b8-9921-6b1027c9014d",
	"3167af1f-c415-461c-8a02-2f3d8ecc93fc",
	"f5e38d4a-2fb6-45c9-ba48-48cada7e9b08",
	"5ac8470c-d730-4313-a6dc-f0691974a494",
	"f5eb435f-9403-494c-be2d-94dc83970994",
	"77d3d00f-7ba4-4384-9336-7e35ef025025",
	"a77548b7-c4ef-4106-8024-8da74f4871b8",
	"68fe9251-7818-4455-828d-ff278f6db08f",
	"1be20e90-8e62-474c-bea1-524cf9255da8",
	"52142ae8-0a8a-4224-bbf8-2242ca29c2a4",
	"d7cdfe3d-f0a3-4502-ba8b-393c7eede0a5",
	"81826ee5-1eaa-4e58-a49b-1cfd8e7d2efd",
	"6844dbc2-569d-41cf-8774-09eabdb65c53",
	"ee32e585-3401-486b-846e-e69905655639",
	"801340f1-c03a-4694-a439-fb0206c86e87",
	"66b17ec2-bbc3-40e7-94f9-601a0bf0ec90",
	"afd6fb07-f66b-4567-bc56-54686a9491a7",
	"730d0a26-8c95-4116-9c76-e1050029cdcb",
	"7570100e-d73a-4d84-ae2f-d5ea0df4d904",
	"d0bf6ccb-3628-4f7b-8da3-99093384305c",
	"ae719401-bfd0-401b-bb65-e54ae617fa77",
	"4be9659d-8409-4027-b011-fcf16af3207a",
	"4c8221a0-7804-4153-a990-d2f2f08c9655",
	"6e27947a-2f3e-4c42-9895-d111f947ac3d",
	"3ed54b96-d537-4e97-ad2e-2c52c777da23",
	"3c6cf8b8-214b-45ed-8b4b-b1e94b0500be",
	"aaa5babe-a949-4de2-a741-38b4d4e93f35",
	"7e781d33-0ab2-4ad1-be63-247c6c4b9476",
	"689314f5-ef66-4439-a90d-feb97862a7ff",
	"93ca949f-3347-475e-8595-bafc23137dd3",
	"4c02e839-42b7-4e4c-8c35-b0544881aa91",
	"c723629c-f6dc-4c32-ad5c-6ada4b1bf236",
	"757f2795-2d50-4d31-8f22-321f0c7bbc71",
	"dbd95595-c1eb-40ea-a8eb-cec762102c7b",
	"df62c4f2-daab-47e3-afdc-0a5b4395fac7",
	"bd1ec39b-f874-49f9-a2ba-16387f8a1b03",
	"02145670-2194-43bd-ac5d-bf0fb56f251a",
	"fad8da10-a2d1-45f3-bea7-f946234b7d0f",
	"e23e8080-6fd7-4052-bfa2-6ad72656faaa",
	"a1000dc0-1b8b-4a85-aaf7-6867cd7eaa07",
	"114a2409-cd47-4da5-a213-6c28fa009b7a",
	"d8f8417b-2c39-480a-889c-4ff056aac916",
	"b6a50c0d-38e1-46dc-b0ba-a8602100f708",
	"65c1ee1f-1781-4f3a-9c04-cab7e37160f2",
	"78bd3187-cbce-4d4c-80bd-bd7e0fdb8478",
	"6542f3db-7b7c-40b0-b251-c1ad110c5936",
	"225a60d8-5aac-4592-a233-7503e747dbbb",
	"05d438bd-b901-4d06-8fde-ef824ae5b29f",
	"8fff8c77-b559-44e1-a440-70a0d41e323a",
	"3ef64bf5-bff9-4835-b0d5-6ae4a299ab20",
	"d8331dc0-2bf5-45a2-af11-67baa2a29313",
	"5f92f242-e064-4e1b-800f-63b8430166c7",
	"f57afbec-36ab-4667-b12d-669b7d2e68b9",
	"105687ba-f919-4cc1-8532-c07ea954f1f7",
	"d7c8bc07-fc03-4b4d-87fc-1b3794bafa44",
	"2d3d79ea-39ce-4b4b-b4e9-5a47f9e3d6b7",
	"b5a4a9f5-f991-49e8-a742-a9bf263b8fbe",
	"30e32df3-7a0e-4c7b-b7f0-89b5d0e32f18",
	"56430d89-db87-4782-ae62-3fddaac2e1f3",
	"729f5f8e-a637-4553-9947-3834cab017e0",
	"128f3883-4aff-4af9-97e0-4b368330876b",
	"3b8831a2-d179-47a4-88ee-36ee40b4c347",
	"ca924165-e042-40a8-ab5c-7a994fd67685",
	"4bc625ce-8a3a-416f-9acd-f63ae311484a",
	"3cc9bd16-20c4-4d03-93a2-e61bb581d6b2",
	"0002e00a-f8d0-491c-af7b-28d6853442fb",
	"22d96dfc-3fcd-493f-888a-fb18bffaa734",
	"0c914312-161a-4bd1-bfb3-c18da290cae6",
	"3860ccd2-2230-46aa-b090-fa45297ac844",
	"c197175d-e0c5-48f1-b0bc-9e7e02106197",
	"64c08667-cb31-41c9-8c9d-e6cda72e4b82",
	"7436f3ff-3212-4477-923f-80e3dadb1a43",
	"fd296309-7a7c-418f-ae5d-afb26534da01",
	"c1d880e3-296b-4609-820f-9ae61c0c980c",
	"a2a861db-b140-4b01-b64e-7e91f7c7c282",
	"bdf5638c-d03e-40b0-a38e-3336230a774e",
	"b5363fd1-e055-4089-a6d2-7858a1dfef78",
	"15d18369-4b35-40d4-893f-33d3b3e0edfd",
	"5941f8b7-d0d9-458d-a4c5-675aee2b7fb4",
	"21f2833f-dd5e-4e5d-a308-83348e6986e4",
	"93294ccb-79b7-4479-aee0-78080998f560",
	"e9d477be-a4ef-4a71-9925-3217eb045928",
	"321c57b8-3a8e-43c3-8497-01ad5ea16746",
	"8e6435de-128c-4a71-9c99-53b5d94cbc22",
	"4fd8aabb-50f6-403f-bbc1-d0b509db0acf",
	"9d2af0b2-01c3-4225-9718-1285604afe4a",
	"aded2beb-800e-4575-bbe4-f6ea423cd1a8",
	"730d908e-b467-445b-846b-e743fd8e3d9f",
	"f337e7fc-ae75-4fa1-9ad3-16efee36f8ef",
	"b4efc389-a6c5-4abd-819a-99bb7d9e6b37",
	"595ba4ce-1c3f-4f85-9a9d-af87dec32df1",
	"2ef36c59-f522-4bde-9a97-ac8ac018e9ed",
	"5231de75-86df-4b60-92be-e3e4090fb952",
	"31237879-5511-4f6a-83e5-7db3463e1f1b",
	"e51ecbef-3205-42d0-9884-7b5947381538",
	"97e10354-0c1c-4eb8-a940-2e2492543017",
	"7ade913e-c811-4cbd-92f1-37ae74004753",
	"6d6bbfaa-c5b6-4299-a1e2-00d9b74b8edc",
	"a7a86e75-6549-42d2-bc35-2014f9ed7d51",
	"4f87530e-033a-4113-8fa7-b05aabd6956d",
	"ac0fb60f-0a51-4fc0-9914-ba36df21a705",
	"24c2b440-e932-40df-a091-786d396a95a4",
	"79caa632-1a59-4b52-8eb2-36f0c7fac28b",
	"d58180e1-a65f-43cd-bb72-8a512ca1c6ee",
	"524aae5b-3c13-49c9-b7e5-6a0dea6ee424",
	"c81e56ce-a956-4161-91be-d6ea08973140",
	"791ab444-cb46-4a82-bce5-7e05d08e6b41",
	"e311175c-9251-4e82-860e-43cd19e074d2",
	"5d0235c6-b70f-4d49-a1f8-38d87c8c861a",
	"7f1795ce-ac77-40e2-afe9-4c190658db99",
	"5d449e4e-d48a-4058-876f-4991b9094bdc",
	"89ec21e8-9a36-4fef-a264-e9a8ee7f017f",
	"07dd984f-9a1b-4ad7-bdc1-2a060183fe5a",
	"f3fefd6c-abdf-4781-b906-f59083432e29",
	"a694b8fe-51b5-4116-bf87-a708269ff1da",
	"5b1f1c19-8945-4284-b4aa-06cbcc14f4ff",
	"802fb40f-e860-4bdf-b7ad-849e34f71f5b",
	"0c24e392-3eed-4b69-8be3-af53eeff2a04",
	"aff54a9f-fdf8-4e39-bbe5-fde3ef1f74eb",
	"48c2dd85-5e7b-4bd2-8b2d-067061e63d11",
	"bc0f5b20-776d-4dd8-9c4a-e937e3aa486e",
	"daf649f3-5900-4778-a05f-ca94da62a2c5",
	"291a6af6-1a34-4f34-b48f-02a410818329",
	"613a929f-236e-4ac4-a7f6-18f10482becb",
	"ca64b7ce-9c82-4984-8063-450214899118",
	"59521242-25b6-44ac-86c3-e78e5761d78e",
	"16525ab6-d5e0-497e-bebe-2fe3396f80d4",
	"5fe5df41-48e3-4e54-b32e-5b5dd923e7eb",
	"ec3178bc-1fb4-4e49-ad57-eaf259d8d621",
	"27631a6d-580c-45c3-baef-165ce5925540",
	"25b6a1ce-e059-4b3a-8a59-15270ad3f81b",
	"55049215-1cf4-4b11-8e86-75131b715cba",
	"193ae680-4905-47a5-ac42-bc1198b67953",
	"90cf1051-6049-441d-9221-7e4a4cda5a62",
	"f50be9d3-18fc-4f93-8c13-9b27918d41fa",
	"397a2c6e-e04d-4afd-8fc2-72aa70693947",
	"fa22dc16-a8ae-4d15-8906-dda9040fef18",
	"34209956-9779-4cec-ba5a-6e5ebc820ab4",
	"5e56ed4e-6473-4d8e-912a-4ecfb5880bf4",
	"5597eb9e-51c8-4590-80cf-86667cfcd3ab",
	"ad5b1ae2-541f-4662-a8d0-e042f983ae87",
	"7de3b449-ed4e-4d25-b61f-c5266829c54d",
	"0edb1765-5bde-4c08-aafe-969d5925c79b",
	"54046dc4-1fb3-4065-a922-5d0b1ac484a8",
	"0d5db33e-bd91-42e0-a220-66863fed30d6",
	"626cb208-132e-4de1-aeb0-e33fd7895ada",
	"29b41ed5-4c84-482a-b262-de2689dd95d9",
	"445aef27-03a3-4bcf-bac6-264271038ea6",
	"81784376-03a3-41fa-ad30-5d72facf6a6e",
	"e185b9a2-6dec-40b7-88ea-8589d176d05b",
	"49d01ff2-8058-4910-8847-eb65d5e4db44",
	"831ec3c7-37a2-46a2-91d8-dc67dacb3159",
	"df9cfe76-9011-480e-a545-a482e962ea67",
	"b3c3a1ba-a380-4ef0-832b-4fa83d72340e",
	"ff1f9a29-bd20-4f4e-9e74-b3815486ac65",
	"6528d0da-9b6f-46b0-87fb-37d2ff841168",
	"54945d8d-ed9f-42c2-9f42-9f5ee279b953",
	"a7ab63a3-4305-42d0-a8af-129ff8acd573",
	"ec84b481-fe72-4fda-ad49-77d1beb57861",
	"89277631-97f8-42b4-b3ca-895f8971b344",
	"28c171ec-ebd8-44e2-a17b-e7e078986cd0",
	"cf35faea-6533-4d1a-81da-711b1fde2a3b",
	"a476da90-6d32-43f3-941d-a76845b5f663",
	"a0eaaabb-2aa3-4f4f-b4e8-2eb08952fc3e",
	"e071c9c1-8c3a-478e-bc68-79a4a54e9745",
	"acb67777-4d73-4d6a-9b16-14e54a13f4d3",
	"8244baa0-736c-410b-b88a-4f40f707c3f8",
	"d371f3b2-608a-43e6-b7e8-4d474e8617e0",
	"6002b539-732c-4c3b-9057-95c653e7d172",
	"3ee9afc4-2ab5-4f7c-9ed4-1d170c8bd2b5",
	"9c2f3cbb-a9a6-46a5-ba86-89c418320d87",
	"772433c8-9abd-45de-8e11-e5c6839a37fb",
	"d979f5be-bb6a-479f-b4dd-664883a553db",
	"e7916829-e82a-4821-8f1d-fe341b187d1b",
	"ca327652-9dc9-482e-b413-37270f12df7a",
	"2bacb332-b3f5-4f18-b237-bffdb4bdbb4a",
	"104cfa78-eb36-4d91-97d7-94e6460068a8",
	"4d6e5f1c-55bd-4fb0-a825-53e0ce637755",
	"287304c3-96fb-48e6-baf2-cd8c17fba5ef",
	"704d4cbc-3c16-4ad2-ad13-260b277b3b4d",
	"f0004ee5-4675-4074-b0e9-b652606da2bc",
	"ad3e45b1-8997-4770-b80f-adb512f5aec5",
	"359e10a3-32a5-4001-afdd-14d850c7f8af",
	"f5ba3572-a46e-4aa7-b8bf-84b983d615e1",
	"c9e34290-62ce-4743-8bb5-26e2b69d7cdc",
	"c996dffe-e1f1-4b71-af2e-e708205fed2c",
	"2f486545-4dde-43c9-ac07-f8a6b0c486ce",
	"f529ad48-dde8-4054-8c7d-af32b7ff730d",
	"8a09bb91-04e3-4fe6-a765-5f5a611854cd",
	"fea622c4-bc74-4b75-8c85-1f8c2bfa850b",
	"243c9b43-5ac3-45ac-952f-6579ca21633a",
	"f6018ed2-6174-476b-a268-d35521b7d7a3",
	"54f2bbc1-7942-41ef-b8db-f1d586f2f5c4",
	"00caf783-38c6-4543-a40d-28264ddb89a6",
	"b85680cc-6b84-4ccf-9587-69fda055ec7a",
	"ab89cced-a52e-46ad-9038-fc8d0a1d1b88",
	"102e4b98-53af-4981-9805-86fa245859cd",
	"49167482-efd5-4b93-af81-cb2c1c2c765b",
	"a02da77c-147e-4eed-8409-6d67b3cc3f96",
	"86c7eb36-b5e5-47e0-9e56-4d94c6a95ac5",
	"ce7ab768-3fce-469a-831f-b32fcd88dff9",
	"6fe24577-1a16-4652-8c75-45e3460c0a8a",
	"dfdaf194-f335-4655-b289-98f64953b8e8",
	"c3499811-856c-424c-9d2f-7fffb99df204",
	"f908a09c-2e7b-44cf-9026-ffaeeded2874",
	"60c2b4b4-33a1-435f-a49a-16d35de16829",
	"a66e3e62-036a-4748-baab-4cdb32e074cc",
	"be6fdde0-52cc-458a-b17c-b5a2bde1f8b0",
	"c2577c39-ac3a-4642-8184-4a7f25472698",
	"3f190346-111e-4998-9a52-a563ecff24ef",
	"4d7795c2-8c63-48de-8b93-3e322425e4fe",
	"b092afa0-5f46-45a4-aba9-499726d12dc0",
	"121c6aac-5d24-493e-ba2e-54ac570e0c58",
	"09ec262c-e70c-4dfb-9c38-4065824217fd",
	"dffa1679-1429-4cef-9765-01b56c93e1c2",
	"b160c879-1a9d-47f9-b872-444e1500b34c",
	"3784d1f1-613e-4731-a26e-af6c3b224b53",
	"54cae3e4-70b3-48e4-9a9d-e0a0c3bcad57",
	"8412dcee-b037-430e-9eab-a99c151e1479",
	"973bb925-c9ca-4f8f-b55c-0d6612576107",
	"39ef7e0e-5e1f-4de4-932e-f35839b763e4",
	"86ac25a6-7117-47d3-8e86-075c4977895f",
	"e5af9230-a719-4841-abff-2fd18a49331e",
	"e63e3cd2-4b4f-47be-a483-45b5a7b76769",
	"00e47276-0afe-4ac6-bece-93b95a34eceb",
	"ab337a17-e122-4abd-a04f-3bc36432c90d",
	"90a31de8-86ef-4fa6-990c-c582c151adfc",
	"d9a91e58-ad6a-4a09-8394-7d186ab408cd",
	"a1e872d3-cb00-42ad-aed1-28a630a21668",
	"9bcb1661-e7a6-4274-a8b9-010424759d40",
	"f2f8a919-a8d5-4585-b03a-2a5f7b2e43b7",
	"9e9b610d-a907-402a-968c-fc0c7800bbfb",
	"a92648f6-f83a-47c7-8d90-1702e7d0846d",
	"d399c553-87f6-473c-8b70-46d31dd76686",
	"847532d5-c96f-4b91-80eb-39d8e1482b74",
	"8ed7b440-9e41-4e7a-879f-9802e0d29aea",
	"fa4eac82-0329-4a46-8ec6-454b3a9a49d9",
	"88efe5b4-2b10-44b7-8ae7-904c9de2326d",
	"63d089b4-22d0-4d14-93b4-e222a8998a7e",
	"e0feddbc-9168-41bc-9063-b76bad1b17dd",
	"5045701e-7b13-4dd2-b15a-0de5e4662f19",
	"14f6ee59-4b71-4e31-9eea-9e49402d5923",
	"9a6c3237-0f4a-4b3c-a967-ef56ed6e7288",
	"6e5a74c4-6d66-490b-bc8d-f53b6f442e67",
	"95933cda-42dc-428c-9e60-5eb71d86145d",
	"aeb38344-3400-4816-99d5-24d8fee085f6",
	"79ee9890-48ed-42ca-bfcf-01f46e20b7cf",
	"a9ae6986-ea35-4230-bbcf-33fa5192ce50",
	"a25d41ee-dff7-4394-90b1-4cb206626bcb",
	"62a823da-429a-4a79-9f84-1bfb646645fd",
	"2bed9d68-784b-46b4-83a9-db1f23c626c6",
	"c69194fa-16e1-4f61-822a-147c288b31b8",
	"319eb96e-ba84-427e-a2fb-a11ce98434b2",
	"3285d2b8-2b85-4d55-ac8a-e47431d7c043",
	"5f908220-b1ce-4cbd-89d8-e5d36e0b98ba",
	"3f31f9d4-a852-4c53-92fe-39410eac6286",
	"47d1d9bf-4d4d-4c90-9ece-9df961283fa0",
	"473ea1d3-1cf0-40d5-9918-4e220b223e08",
	"c4ebd833-63f5-411d-ba3d-fe7b4fbd3182",
	"41bc8e08-018e-4c89-9bc2-3b407002215a",
	"0ab5e778-b282-4870-8d16-df7a123a1570",
	"8f80fd2f-4873-43b9-b9ff-5d2a0112e369",
	"d40f014f-1092-401e-988f-cc7530c78b84",
	"246af7e2-29c7-4b54-9797-1cc8fd65b2e4",
	"ce7f74c8-8285-4dd8-958e-082c0d6e8128",
	"f2a10973-81ca-43a8-83ba-0bd4967d28e1",
	"79cf8890-75e3-4e0a-89ed-d5eeb9996a0f",
	"66a4fd5c-ce51-4d16-a755-46cbb8e6c275",
	"4009c26d-7b5b-4c27-a408-4c86bfad9fd9",
	"95929ad9-789c-4765-a23b-b570c3decb97",
	"d47f7073-479d-4d14-81ef-08087d9161f1",
	"0d8630cb-c1f5-49a6-a2a8-b95bdcb61e80",
	"db6aff42-ef1b-4e26-97a0-45bd7d284e8b",
]

# Tạo câu lệnh SQL để chèn dữ liệu vào bảng Like
insert_sql_like = 'INSERT INTO public."Like" ("likeId", "userId", "songId", "createdAt", "updatedAt") VALUES\n'

# Tạo danh sách các giá trị để chèn vào bảng
values_like = []
for user_id in user_ids:
    liked_songs = set()  # Sử dụng set để tránh trùng lặp bài hát
    num_likes = random.randint(1, len(song_ids))  # Số lượng bài hát mà user sẽ like
    for _ in range(num_likes):
        while True:
            song_id = random.choice(song_ids)
            if song_id not in liked_songs:
                liked_songs.add(song_id)
                break
        
        like_id = str(uuid.uuid4())
        
        # Tạo giá trị createdAt ngẫu nhiên trong vòng 7 ngày qua
        created_at = datetime.now() - timedelta(days=random.randint(0, 7))
        created_at_str = created_at.strftime('%Y-%m-%d %H:%M:%S')
        
        values_like.append(f"('{like_id}', '{user_id}', '{song_id}', '{created_at_str}', '{created_at_str}')")

# Kết hợp các giá trị vào câu lệnh SQL
insert_sql_like += ",\n".join(values_like) + ";"

# Ghi câu lệnh SQL vào file
sql_file_path = 'D:/DUT/NAM4-KI1/PBL6/CRAWL/crawl-data-from-spotify/SQL2/likes_sql.sql'
with open(sql_file_path, 'w', encoding='utf-8') as file:
    file.write(insert_sql_like)

print(f"Câu lệnh SQL đã được ghi vào file: {sql_file_path}")