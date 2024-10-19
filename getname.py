import os

folder = 'D:/DUT/NAM4-KI1/PBL6/AUDIO/'


for folder in os.listdir(folder):
    print(folder.strip())
