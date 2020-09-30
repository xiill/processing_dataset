

#'/home/tati/Рабочий стол/DataSet2/dev-clean (1)/LibriSpeech/dev-clean/        422/137823/251-137823.trans.txt'
import csv
import os

filename11 = '/home/tati/Рабочий стол/DataSet2/dev-clean (1)/LibriSpeech/dev-clean/'
filename111 = '8842'
filename1111 = '304647'
filename11111 = '.trans.txt'
filename1 = filename11 + filename111 + '/' + filename1111 + '/' +  filename111 + '-' + filename1111 + filename11111

filename2 = 'texts/'
filename3 = '/home/tati/Рабочий стол/DataSet2/dev-clean (1)/LibriSpeech/dev-clean/' + filename111 + '/' + filename1111 + '/'

filename4 = 'audio_clips/'


with open(filename1, 'r+', newline='') as csv_file:
    reader = csv.reader(csv_file, delimiter="\n")
    for row in reader:
        i = row[0]
        to_txt = i.split(' ', 1)
        name = to_txt[0]
        texts = to_txt[1]
        with open(filename2 + name + '.csv', 'w+') as txt:
            txt.write(name + '|' + texts)
        # audio_files_to_directories
        # AUDIO
        if not os.path.isdir(filename4 + name):
            os.mkdir(filename4 + name)
        os.replace(filename3 + name + '.flac', filename4 + name + '/' + name + '.flac')
# переименоание аудио файла из flac в wav
list_dir =os.listdir(path="audio_clips")

for i in range(0,2703):
    if  os.path.exists('audio_clips/' + list_dir[i] + '/' + list_dir[i] + '.flac'):
        os.rename('audio_clips/' + list_dir[i] + '/' + list_dir[i] + '.flac', 'audio_clips/' + list_dir[i] + '/' + list_dir[i] + '.wav')


