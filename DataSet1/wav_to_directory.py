"""Создание директория, имеющие название как и аудио файлов"""
import os
import csv

filename1 = 'metadata.csv'
filename2 = 'audio_clips/'
filename3 = '/'

filename5 = '.wav'

with open(filename1, 'r', newline='') as csv_file:
    reader = csv.reader(csv_file, delimiter="\n")
    for row in reader:
        i = row[0]
        to_txt = i.split('|', 3)
        """"Создание директории"""
        #os.mkdir(filename2 + to_txt[0])
        """"Перемещение .wav в директорию с таким же именем"""
        os.replace(filename2+to_txt[0]+ filename5, filename2+to_txt[0]+ filename3 +to_txt[0]+filename5)


